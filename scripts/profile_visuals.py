#!/usr/bin/env python3
"""Generate small, self-contained profile SVGs from GitHub data.

No image service, browser-side script, user PAT, or external SVG/font assets.
Only aggregate activity and PUBLIC owned-repository metadata are saved.
A failed fetch leaves the previous committed SVGs untouched.
"""
from __future__ import annotations
import datetime as dt
import html
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'generated'
USER = 'zeron-G'
BG, PANEL, INK, DIM, GOLD, ICE = '#0d1724', '#142330', '#e8eeed', '#9db4c2', '#ebbc84', '#95d9de'


def request(url: str, payload: dict | None = None, authenticated: bool = True) -> dict:
    headers = {'User-Agent': 'Rongze-profile-visuals', 'Accept': 'application/vnd.github+json'}
    token = os.environ.get('GH_TOKEN')
    if authenticated and token:
        headers['Authorization'] = 'Bearer ' + token
    data = None if payload is None else json.dumps(payload).encode()
    if data:
        headers['Content-Type'] = 'application/json'
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=25) as response:
                result = json.load(response)
            if isinstance(result, dict) and result.get('errors'):
                raise RuntimeError('GitHub GraphQL error: ' + '; '.join(e.get('message', 'Unknown') for e in result['errors']))
            return result
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError('Request did not complete')


def probe_previous_services() -> None:
    """Diagnostic only; images do not depend on these services any more."""
    urls = [
        'https://github-readme-activity-graph.vercel.app/graph?username=zeron-G',
        'https://github-profile-trophy.vercel.app/?username=zeron-G&theme=tokyonight',
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                prefix = response.read(100).decode('utf-8', errors='replace')
                print(json.dumps({'previous_service': url, 'status': response.status, 'content_type': response.headers.get('Content-Type'), 'body_prefix': prefix}))
        except urllib.error.HTTPError as error:
            print(json.dumps({'previous_service': url, 'status': error.code, 'body_prefix': error.read(100).decode('utf-8', errors='replace')}))
        except Exception as error:
            print(json.dumps({'previous_service': url, 'error': type(error).__name__}))


def collect() -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    start = (now - dt.timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0)
    query = '''query($login:String!,$from:DateTime!,$to:DateTime!){
      user(login:$login){
        contributionsCollection(from:$from,to:$to){
          contributionCalendar{weeks{contributionDays{date contributionCount}}}
        }
      }
    }'''
    result = request('https://api.github.com/graphql', {'query': query, 'variables': {
        'login': USER, 'from': start.isoformat(), 'to': now.isoformat()}})
    days = sorted((d for w in result['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
                   for d in w['contributionDays'] if start.date().isoformat() <= d['date'] <= now.date().isoformat()), key=lambda x: x['date'])
    expected = [(start.date() + dt.timedelta(days=i)).isoformat() for i in range(31)]
    if [d['date'] for d in days] != expected or any(not isinstance(d['contributionCount'], int) or d['contributionCount'] < 0 for d in days):
        raise RuntimeError('Incomplete contribution calendar; retaining last good images')
    # Anonymous REST calls explicitly restrict these cards to public metadata.
    user = request(f'https://api.github.com/users/{USER}', authenticated=False)
    repos = []
    page = 1
    while True:
        batch = request(f'https://api.github.com/users/{USER}/repos?per_page=100&type=owner&page={page}', authenticated=False)
        if not isinstance(batch, list):
            raise RuntimeError('Invalid public repository response')
        repos.extend(r for r in batch if not r.get('private') and not r.get('fork') and r.get('owner', {}).get('login', '').lower() == USER.lower())
        if len(batch) < 100:
            break
        page += 1
        if page > 30:
            raise RuntimeError('Unexpected repository pagination')
    count = sum(d['contributionCount'] for d in days)
    return {'user': USER, 'updated_at': now.strftime('%Y-%m-%dT%H:%M:%SZ'), 'scope': 'GitHub-reported 31-day contributions; public owned non-fork repositories; no private repository details',
            'days': days, 'contributions_31d': count, 'active_days_31d': sum(d['contributionCount'] > 0 for d in days),
            'public_owned_repositories': len(repos), 'stars_public_owned': sum(r['stargazers_count'] for r in repos),
            'forks_public_owned': sum(r['forks_count'] for r in repos), 'followers': user['followers']}


def text(x: float, y: float, value: object, size: int = 12, color: str = INK, extra: str = '') -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" {extra}>{html.escape(str(value))}</text>'


def shell(title: str, desc: str, height: int, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>
<style>text{{font-family:Arial,Helvetica,sans-serif}}.pulse{{animation:glow 5s ease-in-out infinite}}.trace{{stroke-dasharray:1;stroke-dashoffset:0;animation:trace 9s ease-in-out infinite}}.medal{{transform-box:fill-box;transform-origin:center;animation:float 5s ease-in-out infinite}}@keyframes trace{{0%{{stroke-dashoffset:1}}45%,100%{{stroke-dashoffset:0}}}}@keyframes glow{{0%,100%{{opacity:.45}}50%{{opacity:1}}}}@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-3px)}}}}@media(prefers-reduced-motion:reduce){{.pulse,.trace,.medal{{animation:none}}}}</style>
<defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{ICE}" stop-opacity=".24"/><stop offset="1" stop-color="{ICE}" stop-opacity=".015"/></linearGradient></defs>
<rect width="1200" height="{height}" rx="14" fill="{BG}"/><rect x=".5" y=".5" width="1199" height="{height-1}" rx="14" stroke="#294151" fill="none"/>{body}</svg>\n'''


def activity(snapshot: dict) -> str:
    days = snapshot['days']
    counts = [d['contributionCount'] for d in days]
    ceiling = max(4, math.ceil(max(counts) / 4) * 4)
    x0, x1, y0, y1 = 66, 1146, 115, 292
    coords = [(x0 + i * (x1 - x0) / 30, y1 - n / ceiling * (y1 - y0)) for i, n in enumerate(counts)]
    path = 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in coords)
    body = text(34, 39, 'CONTRIBUTION FLIGHT PATH', 18, INK, 'letter-spacing="2"')
    body += text(34, 67, f"{snapshot['contributions_31d']:,} contributions · {snapshot['active_days_31d']} active days · last 31 days", 12, DIM)
    body += text(1166, 39, '@' + USER, 12, GOLD, 'text-anchor="end"')
    for i in range(5):
        y = y1 - i * (y1 - y0) / 4
        body += f'<path d="M{x0} {y}H{x1}" stroke="#29404f" stroke-width="1"/>'
        body += text(50, y + 4, int(ceiling * i / 4), 10, DIM, 'text-anchor="end"')
    body += f'<path d="{path} L{x1},{y1} L{x0},{y1}Z" fill="url(#area)"/>'
    body += f'<path d="{path}" stroke="{ICE}" stroke-opacity=".28" stroke-width="2" fill="none"/>'
    body += f'<path class="trace" pathLength="1" d="{path}" stroke="{GOLD}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    for (x, y), day in zip(coords, days):
        body += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3" fill="{ICE}"><title>{day["date"]}: {day["contributionCount"]} contributions</title></circle>'
    for i in [0, 5, 10, 15, 20, 25, 30]:
        body += text(coords[i][0], 315, days[i]['date'][5:], 10, DIM, 'text-anchor="middle"')
    body += text(34, 353, 'GitHub-reported contributions · daily snapshot · today may be partial', 10, DIM)
    body += text(1166, 353, 'Updated ' + snapshot['updated_at'][:10] + ' UTC', 10, DIM, 'text-anchor="end"')
    return shell('Rongze Gao contribution activity', 'Animated line over a real 31-day contribution snapshot. ' + snapshot['scope'], 375, body)


def trophies(snapshot: dict) -> str:
    metrics = [('REPOSITORIES', 'public · owned · non-fork', snapshot['public_owned_repositories']),
               ('STARS', 'public owned repositories', snapshot['stars_public_owned']),
               ('FORKS', 'public owned repositories', snapshot['forks_public_owned']),
               ('FOLLOWERS', 'GitHub followers', snapshot['followers']),
               ('CONTRIBUTIONS', 'last 31 days', snapshot['contributions_31d']),
               ('ACTIVE DAYS', 'last 31 days', snapshot['active_days_31d'])]
    body = text(34, 37, 'GITHUB MILESTONES', 17, INK, 'letter-spacing="2"')
    body += text(1166, 37, 'PUBLIC PROFILE / ' + snapshot['updated_at'][:10], 10, DIM, 'text-anchor="end"')
    for i, (label, scope, value) in enumerate(metrics):
        x = 28 + i * 193
        body += f'<rect x="{x}" y="57" width="179" height="185" rx="8" fill="{PANEL}" stroke="#2a4352"/>'
        body += f'<g class="medal" style="animation-delay:{i*.35}s" fill="none" stroke="{GOLD}" stroke-width="1.7"><path d="M{x+75} 79h29v17q0 17-14.5 17T{x+75} 96Z"/><path d="M{x+75} 82h-9v7q0 11 11 11m27-18h9v7q0 11-11 11m-12 13v10m-9 0h18"/><path d="m{x+89.5} 84 2.5 5.5 6 .5-4.5 4 1.5 6-5.5-3-5.5 3 1.5-6-4.5-4 6-.5Z" fill="{GOLD}" stroke="none"/></g>'
        body += text(x+89.5, 166, f'{value:,}', 32, INK, 'text-anchor="middle"')
        body += text(x+89.5, 192, label, 10, GOLD, 'text-anchor="middle" letter-spacing="1"')
        body += text(x+89.5, 215, scope, 9, DIM, 'text-anchor="middle"')
    body += text(34, 268, 'Self-hosted statistics · not official GitHub awards or the third-party S/SSS ranking system', 10, DIM)
    return shell('Rongze Gao GitHub milestone trophies', 'Trophy-style cards with actual public statistics. No invented ranks.', 287, body)


def patch_readmes() -> None:
    notes = {
      'README.md': '<sub>Contribution and milestone SVGs are generated daily in this repository from GitHub data. The cards show real statistics, not official GitHub awards. If a refresh fails, the last successful snapshot stays visible.</sub>',
      'README.zh-CN.md': '<sub>贡献图与奖杯风格统计卡由本仓库每日生成，数据来自 GitHub；卡片显示实际统计，不代表 GitHub 官方奖项。刷新失败时保留上次成功的快照。</sub>',
    }
    for name, note in notes.items():
        path = ROOT / name
        source = path.read_text(encoding='utf-8')
        updated = re.sub(r'src="https://github-readme-activity-graph\.vercel\.app/[^"\s]*"', 'src="./assets/generated/contribution-activity.svg"', source)
        updated = re.sub(r'src="https://github-profile-trophy\.vercel\.app/[^"\s]*"', 'src="./assets/generated/profile-trophies.svg"', updated)
        updated = re.sub(r'<sub>Activity and trophy images.*?</sub>', note, updated)
        updated = re.sub(r'<sub>活动图与奖杯由外部服务提供.*?</sub>', note, updated)
        if updated != source:
            path.write_text(updated, encoding='utf-8')


def main() -> None:
    if '--probe' in sys.argv:
        probe_previous_services()
    data = collect()
    images = {'contribution-activity.svg': activity(data), 'profile-trophies.svg': trophies(data)}
    for value in images.values():
        parsed = ET.fromstring(value)
        if parsed.tag != '{http://www.w3.org/2000/svg}svg' or '<script' in value.lower() or '<foreignObject' in value:
            raise RuntimeError('Invalid generated SVG')
    OUT.mkdir(parents=True, exist_ok=True)
    for name, value in images.items():
        (OUT / name).write_text(value, encoding='utf-8')
    (OUT / 'snapshot.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    patch_readmes()
    print(json.dumps({'status': 'generated', 'updated_at': data['updated_at'], 'days': len(data['days']), 'images': list(images), 'contributions_31d': data['contributions_31d'], 'public_owned_repositories': data['public_owned_repositories']}))


if __name__ == '__main__':
    main()
