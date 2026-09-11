<a href="https://rongzegao.com"><img width="100%" alt="Rongze Gao — intelligence beyond the screen" src="./assets/observatory-header.svg"></a>

<p align="center">
  <a href="https://rongzegao.com"><b>EXPLORE THE PORTFOLIO ↗</b></a>
  &nbsp; · &nbsp; <a href="./README.zh-CN.md">简体中文</a>
  &nbsp; · &nbsp; <a href="mailto:rgao28@jh.edu">Email</a>
  &nbsp; · &nbsp; <a href="https://www.linkedin.com/in/rongze-gao-09b488303/">LinkedIn</a>
</p>

<br>

## 01 / Intelligence, made tangible

I’m **Rongze Gao / 高荣泽**, a Johns Hopkins M.S. graduate working on **persistent AI agents, healthcare research and systems engineering**. At [CDHAI](https://cdhai.carey.jhu.edu/ai-agent-lab/), I work with [Professor Gordon Gao](https://carey.jhu.edu/faculty/faculty-directory/gordon-gao-phd) on patient-data analysis and personalized forecasting. Outside the lab, I develop agent runtimes and cross-language infrastructure, and support U.S.-market robot deployment and maintenance at Tuskrobots.

**Models are only part of the system.** I care about how data enters, how tools act, how failures recover, and how results can be independently checked.

<br>

## 02 / Selected systems

<a href="https://rongzegao.com/?lang=en#project/anima-family"><img width="100%" alt="01 — ANIMA / ANIMA² — persistent agent systems" src="./assets/anima.svg"></a>

### ANIMA / ANIMA² · From conversations to continuous work

Independently built ANIMA’s modular agent framework and reimplemented ANIMA² around a shared asynchronous Python runtime, React/TypeScript Web interface, Textual terminal and SQLite WAL state.

- **Continuity:** persistent sessions, sourced memory, correction and forgetting; on-demand tool loading, hashed artifacts and exact-evidence recovery after context archival.
- **Controlled execution:** approvals, revocation, atomic edits and process-tree cancellation; subprocess contract tests, versioned plugin activation and rollback without modifying the kernel.
- **Distributed work:** SSH node discovery, parallel delegation, artifact return and explicit memory-sync conflict handling, with recorded Windows/Linux three-agent acceptance journeys.
- **Verification:** code repair against untouched tests, real browser form submission and reconnect recovery; September 9 records include 216 Python tests, 30 Web unit tests and 15 browser scenarios. These are project acceptance records, not a benchmark-ranking claim.

[Case study ↗](https://rongzegao.com/?lang=en#project/anima-family) · [ANIMA · private](https://github.com/zeron-G/anima) · [ANIMA² · private](https://github.com/zeron-G/anima2) · [Verification ledger](https://github.com/zeron-G/anima2/blob/main/specs/001-anima2/verification.md)

<br>

<a href="https://rongzegao.com/?lang=en#project/synapse"><img width="100%" alt="02 — Synapse — cross-language shared-memory infrastructure" src="./assets/synapse.svg"></a>

### Synapse · Different languages, one data contract

Built a **Rust shared-memory bridge** between Python AI processes and native C++/Rust applications, retaining explicit process boundaries and shared type definitions.

- Implemented bidirectional **SPSC ring buffers**, Linux POSIX / Windows memory-mapping wrappers, Python native/mmap access and a C++ header-only client.
- Developed the **.bridge IDL** lexer, parser, C ABI layout computation and generators for Rust structures, Python ctypes and C++ definitions with layout assertions.
- Added typed channels, **seqlock latest-value slots**, configurable waiting, heartbeats, peer-exit detection and graceful cleanup, with round-trip, layout and failure-path tests.

[Case study ↗](https://rongzegao.com/?lang=en#project/synapse) · [Source](https://github.com/zeron-G/Synapse) · [Benchmark methodology](https://github.com/zeron-G/Synapse/blob/main/benchmarks/README.md)

<br>

<a href="https://rongzegao.com/?lang=en#project/hapf"><img width="100%" alt="03 — HAPF — shared knowledge, personal predictions" src="./assets/hapf.svg"></a>

### HAPF & patient-data agents · Evidence before eloquence

At CDHAI, developed a research pipeline connecting **population training, low-rank patient adaptation, uncertainty calibration and population fallback** for 30/60-minute glucose forecasting.

- Built causal TCN modeling and subject-safe chronological evaluation, preventing the same person’s records or future observations from leaking into training.
- Conducted exploratory leave-one-subject-out evaluation on **12 CGM subjects**. Personalization was accepted in 6 of 12 folds; the small sample does not establish clinical effectiveness.
- In **CDHAI_June**, organized patient-file ingestion, deterministic statistics, hypothesis checks, evidence ledgers and LLM reporting, with reusable artifacts and HAPF integration.

[HAPF case study ↗](https://rongzegao.com/?lang=en#project/hapf) · [Model repository](https://github.com/zeron-G/CDHAI-HAPF) · [Protocol & results](https://github.com/zeron-G/CDHAI-HAPF/blob/main/docs/proof_of_concept.md) · [Patient-data agent](https://github.com/zeron-G/CDHAI_June)

> Private links require repository permission; walkthroughs can be arranged directly. Medical projects are research prototypes, not diagnostic products or insulin-dosing systems. Performance and test claims should be read with their linked scope and conditions.

<br>

## 03 / More of the workshop

| Project | What it explores | Context |
| :--- | :--- | :--- |
| [Virtual Teaching Assistant](https://rongzegao.com/?lang=en#project/vta) | Independently developed teaching-support application | Carey teaching pilot |
| [PiDog / embodied-robot](https://rongzegao.com/?lang=en#project/pidog) | Layered device control, voice and remote-AI interaction on existing hardware | Personal prototype · private |
| [mech](https://github.com/zeron-G/mech) | Powered-exoskeleton architecture, sensing and staged safety validation | Planning / technical design |
| [Kinsoul / SoulPack](https://rongzegao.com/?lang=en#project/kinsoul) | Persistent personas, memory and portable-state semantics | Product prototype / format draft |
| [Alpha Research Agent](https://github.com/zeron-G/worldquant-alpha-research-agent) | Factor exploration, simulation and governed submission | Research automation; not live returns |
| [FinRAG Agent](https://github.com/zeron-G/FinRAG-Agent) | Section-aware 10-K retrieval, streaming answers and source tracing | JHU course-team project |
| [Black Hole Renderer](https://github.com/zeron-G/blackhole-sim) | Schwarzschild ray tracing, lensing and accretion-disk visualization | Personal numerical / visual experiment |

[Explore the complete project index ↗](https://rongzegao.com/?lang=en#work)

<br>

## 04 / Trajectory

| Period | Work |
| :--- | :--- |
| **Jan 2026 – Present** | **Research Assistant · Johns Hopkins CDHAI** — patient forecasting and research agents; sole developer of a VTA used in a Carey teaching pilot. |
| **Feb 2025 – Present** | **Engineering Intern / Part-time Engineer · Tuskrobots** — U.S.-market robot deployment, commissioning, troubleshooting and continued project maintenance. The period combines internship and part-time engagement. |
| **Sep 2025 – Jan 2026** | **AI Specialist · Vital Guardian / JHU Ward Infinity** — device-connected kidney-health monitoring and ML tools; contributed to the [team awarded the $20,000 top prize](https://carey.jhu.edu/news/ward-infinity-makes-path-tech-minded-entrepreneurs-improve-public-health). |
| **Part-time / Remote** | **Research Consultant · WorldQuant BRAIN** — alpha-factor research and out-of-sample analysis. |

<details>
<summary><b>Earlier industry experience</b></summary>

**Hetang Venture Capital / 荷塘创业投资管理有限公司 · Aug–Nov 2024**  
Evaluated eight medical-device investment opportunities through roadshows, startup discussions and financial/technical analysis.

**Guotai Junan Securities, Zhejiang · Jul–Aug 2024**  
Independently developed and promoted a Python tool to retrieve and process business reports for **25 branches**, and researched **23 listed companies**.

**Minsheng Securities, Zhejiang · Jun–Aug 2022**  
Analyzed and organized financial data, establishing context for later modeling and automation work.

</details>

<br>

## 05 / Education & research

| Institution | Qualification |
| :--- | :--- |
| **Johns Hopkins University · 2025–2026** | M.S. Information Systems & Artificial Intelligence · degree conferred August 29, 2026 · **Beta Gamma Sigma** |
| **Hangzhou City University / University of Waikato · 2021–2025** | Dual Finance degrees: Bachelor of Economics & Bachelor of Business · **GPA 3.67/4.0** |
| **CQF Institute · 2023–2024** | Certificate in Quantitative Finance · **Passed with Distinction** |

**Publication**  
Gao, R. (2024). [*Trend Prediction Analysis of Shanghai Composite Index Based on LSTM Neural Network*](https://doi.org/10.54097/qw8hwy64). *Highlights in Business, Economics and Management, 24*, 409–416.

**Selected honors**  
Kaggle Optiver — **Bronze medal** · WorldQuant Challenge 2024 — **Gold Level** · CFA Research Challenge — **Outstanding Investment Research**.

**Research notes**  
[Distributed-agent continuity: bilingual research outline](./research/distributed-agent-continuity/) — exploratory ideas, separate from peer-reviewed publication.

<br>

## 06 / Beyond the terminal

FAA Part 141 private-pilot training at **Washington International Flight Academy**, robotics tinkering and interactive worlds. I enjoy the intersection of procedure, spatial judgment and systems thinking. Training is not presented as a completed pilot certificate.

[Enter the interactive web game ↗](https://rongzegao.com/game.html) · [Read my full background ↗](https://rongzegao.com/?lang=en#profile)

<details>
<summary>Contribution trail</summary>

![Contribution snake](https://raw.githubusercontent.com/zeron-G/zeron-G/output/github-contribution-grid-snake.svg)

</details>

<br>

---

<p align="center"><b>Let’s build something that matters.</b><br><br><a href="mailto:rgao28@jh.edu">rgao28@jh.edu</a> &nbsp; · &nbsp; <a href="https://rongzegao.com">rongzegao.com ↗</a><br><sub>Rongze Gao / 高荣泽 · Observatory 2026 · Public summaries, private source where marked.</sub></p>
