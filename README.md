# David Zhu

**Reliable AI Systems · Backend Engineering · Reproducible Data Science**

I build AI applications where model output is treated as **untrusted input** and product behavior is enforced by deterministic code, explicit validation, tests, CI, fallback paths, and reproducible evidence.

我关注的不是“把模型接进产品”本身，而是怎样把不确定的模型能力放进**可验证、可维护、可复现的软件边界**：模型负责生成与推理，代码负责事实、规则、状态与最终可执行动作。

[Engineering evidence](ENGINEERING.md) · [All projects](PROJECTS.md)

---

## Flagship work

### MediRAG — evidence-aware RAG system

Java/Spring Boot medical knowledge RAG with hybrid retrieval, RRF, reranking, confidence handling, citations, and SSE generation. The evaluation layer distinguishes real qrels from keyword proxies: Recall/MRR is only reported when explicit relevance labels exist.

**Java 17 · Spring Boot · Vue 3 · Milvus · Redis · MinIO**

[Repository](https://github.com/GOOD-123-CPU/medirag-open) · [Architecture](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) · [RAG pipeline](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md)

[![MediRAG CI](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml)

### OpenInterview — failure-aware asynchronous workflow

Resume parsing, structured question generation, speech interview processing, and report generation are coordinated through explicit product state. SQLite task leases use atomic transactions to prevent concurrent workers from processing the same task, while expired leases allow recovery after worker failure.

**Python · Flask · SQLite · Whisper · Docker**

[Repository](https://github.com/GOOD-123-CPU/OpenInterview) · [Architecture / ADR](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/docs/architecture.md) · [Tests](https://github.com/GOOD-123-CPU/OpenInterview/tree/main/app/tests)

[![OpenInterview CI](https://github.com/GOOD-123-CPU/OpenInterview/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/OpenInterview/actions/workflows/ci.yml)

### Itinera — LLM output constrained before product actions

Natural-language plans are parsed into a structured itinerary and checked by deterministic semantic guards: real calendar dates, time ordering, overlap, coordinate validity, and retrieval-bound venue IDs. Executable reservation actions are rebound to canonical database records rather than trusting model-generated names.

**Next.js · TypeScript · Prisma · SQLite · Leaflet**

[Repository](https://github.com/GOOD-123-CPU/itinera) · [Itinerary engine](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [Tests](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts)

[![Itinera CI](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml)

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
| **Model output is untrusted** | retrieval-bound IDs, validation, clamps, abstention/fallback |
| **Failure-aware orchestration** | OpenInterview task leases; bounded concurrency; cleanup and retry paths |
| **Verification** | unit/statistical tests, type checks, production builds, secret/dependency scanning |
| **Reproducibility** | HanBayes frozen artifacts; VoxFrontier run manifests and SHA-256 hashes |

CI proves that automated checks passed for a specific revision. It does **not** by itself prove model quality, business impact, or production reliability. Those claims require separate benchmarks, integration evidence, or real-world operation.

## More selected work

- **ScreenWeaver** — configuration-driven Vue/ECharts visualization engine with HTTP/WebSocket lifecycle handling and a [live demo](https://good-123-cpu.github.io/screenweaver/).
- **HanBayes** — interpretable Bayesian Chinese sentiment experiments with exact McNemar tests, seeded paired bootstrap, frozen configuration, and published-artifact consistency checks.
- **VoxFrontier** — reproducible DEA / attribution / Double-ML research pipeline with run manifests and file hashes.
- **Investment Committee** — deterministic quantitative core wrapped by multi-agent research and risk-review workflows.
- **LexAtlas / NutriMentor** — domain RAG systems showing the same reliability pattern in legal and nutrition contexts.

See the complete, categorized catalog in [PROJECTS.md](PROJECTS.md).

## Public release history

Several projects were developed and iterated locally before being open-sourced together in September 2026, so repository creation dates reflect public release dates rather than original project start dates. I do not rewrite or fabricate historical commits; ongoing engineering changes are recorded normally through issues, commits, pull requests, CI, and releases.

## Contact / technical discussion

For implementation questions, reproducibility issues, or bug reports, please open an issue in the relevant repository with the environment, reproduction steps, expected behavior, and observed behavior.
