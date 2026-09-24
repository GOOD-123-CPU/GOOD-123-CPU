# David Zhu

**Reliable AI Systems · Backend Engineering · Reproducible Data Science**

I build software around a simple rule: **model output is untrusted until deterministic code verifies it**.

我的重点不是“把 AI 接进产品”，而是把不确定的模型能力放进**可验证、可维护、可复现的软件边界**：模型负责生成与推理，代码负责事实、规则、状态与最终可执行动作。

[Engineering evidence](ENGINEERING.md) · [Project catalog](PROJECTS.md)

---

## Flagship engineering work

| Project | Engineering problem | Evidence |
| --- | --- | --- |
| **[MediRAG](https://github.com/GOOD-123-CPU/medirag-open)** | Build a medical RAG pipeline without confusing retrieval proxies with labelled evaluation | Hybrid retrieval + RRF + reranking; explicit qrels-only Recall/MRR contract; CI and evaluation tooling |
| **[OpenInterview](https://github.com/GOOD-123-CPU/OpenInterview)** | Keep asynchronous AI workflows safe under concurrent workers and failures | Atomic SQLite task leases, expiry recovery, multi-version tests, CI |
| **[Itinera](https://github.com/GOOD-123-CPU/itinera)** | Prevent LLM-generated plans from becoming unsafe product actions | Calendar/time/coordinate/ID validation, deterministic fallback, canonical database rebinding |

### MediRAG
Java / Spring Boot · Vue 3 · Milvus · Redis · MinIO

Medical knowledge RAG with hybrid retrieval, reranking, confidence handling, citations, and SSE generation. The evaluation layer reports Recall/MRR only when explicit relevance labels exist and keeps lexical proxy metrics visibly separate.

[Architecture](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) · [RAG pipeline](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md) · [CI](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml)

### OpenInterview
Python · Flask · SQLite · Whisper · Docker

Resume parsing, structured question generation, speech interview processing, and report generation coordinated through explicit product state. Atomic task leases prevent concurrent workers from processing the same entity while expired leases permit recovery after worker failure.

[Architecture / ADR](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/docs/architecture.md) · [Tests](https://github.com/GOOD-123-CPU/OpenInterview/tree/main/app/tests) · [CI](https://github.com/GOOD-123-CPU/OpenInterview/actions/workflows/ci.yml)

### Itinera
Next.js · TypeScript · Prisma · SQLite · Leaflet

Natural-language plans are parsed into structured itineraries and checked by deterministic semantic guards before downstream actions: real calendar dates, time ordering, overlap, coordinate validity, and retrieval-bound IDs.

[Itinerary engine](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [Tests](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts) · [CI](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml)

---

## Engineering pattern

```text
LLM / external input
        ↓
untrusted structured output
        ↓
schema + semantic validation
        ↓
deterministic business rules
        ↓
fallback / rejection / canonical rebinding
        ↓
tests + CI + reproducible evidence
```

| Principle | Public examples |
| --- | --- |
| **Deterministic core** | Itinera semantic guards; Investment Committee numeric scoring |
| **Model output is untrusted** | retrieval-bound IDs, validation, clamps, abstention / fallback |
| **Failure-aware orchestration** | OpenInterview task leases; bounded concurrency; cleanup and retry paths |
| **Verification** | unit/statistical tests, type checks, production builds, secret/dependency scanning |
| **Reproducibility** | HanBayes frozen artifacts; VoxFrontier run manifests and SHA-256 hashes |

> CI proves that automated checks passed for a specific revision. It does **not** by itself prove model quality, business impact, or production reliability. Those require separate benchmarks, integration evidence, or real-world operation.

---

## Selected work

- **[ScreenWeaver](https://github.com/GOOD-123-CPU/screenweaver)** — configuration-driven Vue/ECharts visualization engine with HTTP/WebSocket lifecycle handling and a **[live demo](https://good-123-cpu.github.io/screenweaver/)**.
- **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** — interpretable Bayesian Chinese sentiment experiments with exact McNemar tests, seeded paired bootstrap, frozen configuration, and artifact-consistency checks.
- **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** — reproducible DEA / attribution / Double-ML research pipeline with run manifests and file hashes.
- **[Investment Committee](https://github.com/GOOD-123-CPU/investment-committee)** — deterministic quantitative core wrapped by multi-agent research and risk-review workflows.
- **[LexAtlas](https://github.com/GOOD-123-CPU/LexAtlas)** / **[NutriMentor](https://github.com/GOOD-123-CPU/nutrimentor)** — domain RAG systems showing the same reliability pattern in legal and nutrition contexts.

See the full categorized inventory and repository notes in **[PROJECTS.md](PROJECTS.md)**.

---

## Public release history

Several projects were developed and iterated locally before being open-sourced together in September 2026. Repository creation dates therefore reflect **public release dates**, not necessarily original project start dates.

I do not rewrite or fabricate historical commits. Ongoing engineering changes are recorded normally through issues, commits, pull requests, CI, and releases.

## Contact / technical discussion

For implementation questions, reproducibility issues, or bug reports, open an issue in the relevant repository with the environment, reproduction steps, expected behavior, and observed behavior.
