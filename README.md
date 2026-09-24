# David Zhu

**AI / Software Engineer · Java & TypeScript · Reproducible Data Science**

你好，我是 David Zhu，数据科学与大数据技术背景。我更关注怎样把模型、数据与业务约束组织成**可验证、可维护、可复现的软件系统**：让确定性代码负责事实与规则，让模型负责生成与推理，并通过测试、CI、失败兜底和实验记录把边界写清楚。

I build AI applications and data systems with explicit interfaces, deterministic guardrails, testable components, and reproducible delivery. My work spans Java/Spring backends, TypeScript product engineering, and Python research pipelines.

[工程阅读指南](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/ENGINEERING.md) · [完整项目目录](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/PROJECTS.md)

> **Public release history.** Several projects were developed and iterated locally before being open-sourced together in September 2026. Repository creation dates therefore reflect public release dates rather than project start dates. I do not rewrite or fabricate historical commits; ongoing improvements are recorded normally on GitHub.

## Selected work

### MediRAG · Java RAG backend

把 Query 改写、混合召回、RRF、重排序、置信度判断、引用与 SSE 生成组织为可检查的流水线；MySQL、Milvus、MinIO 与 Redis 分担不同存储职责。评估器强制区分显式 qrels 与关键词 proxy：只有存在 `relevant_doc_ids` 才报告 Recall/MRR，CI 里的合成 fixture 只验证指标契约，不冒充医疗检索效果。

**Java 17 · Spring Boot · Vue 3 · Milvus · Redis · MinIO**

[架构](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) · [RAG 链路](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md) · [仓库](https://github.com/GOOD-123-CPU/medirag-open)

[![MediRAG CI](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml)

### Itinera · AI product workflow

自然语言需求进入产品流程前先被解析成受约束的结构化行程；除字段形状外，代码还检查真实日期、时间顺序/重叠、坐标范围和候选地点 ID。模型提出的可执行预订必须重新绑定到本轮数据库检索得到的 canonical record，否则拒绝并回退。

**Next.js · TypeScript · Prisma · SQLite · Leaflet**

[行程引擎](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [测试](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts) · [仓库](https://github.com/GOOD-123-CPU/itinera)

[![Itinera CI](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml)

### ScreenWeaver · Configuration-driven visualization engine

将 JSON schema、数据源生命周期、组件注册表与 Vue 渲染层拆分。支持 static / mock / HTTP / WebSocket 数据源与 GitHub Pages 在线演示，重点关注数据接入、资源释放和可扩展组件边界。

**Vue 3 · TypeScript · ECharts**

[在线演示](https://good-123-cpu.github.io/screenweaver/) · [架构](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/architecture.md) · [数据源实现](https://github.com/GOOD-123-CPU/screenweaver/blob/main/src/engine/useSources.ts)

[![ScreenWeaver CI](https://github.com/GOOD-123-CPU/screenweaver/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/screenweaver/actions/workflows/ci.yml)

### OpenInterview · Asynchronous AI workflow

从简历解析、结构化出题、语音面试到报告生成形成完整状态流；SQLite `BEGIN IMMEDIATE` task lease 将业务状态与执行所有权分离，多个 worker 不会同时处理同一任务，崩溃后的过期 lease 可恢复。当前 CI 在 Python 3.10/3.11/3.12 上验证 62 个 pytest；AI 评价仍明确定位为辅助信息。

**Python · Flask · SQLite · Whisper · Docker**

[架构与 ADR](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/docs/architecture.md) · [测试](https://github.com/GOOD-123-CPU/OpenInterview/tree/main/app/tests) · [仓库](https://github.com/GOOD-123-CPU/OpenInterview)

[![OpenInterview CI](https://github.com/GOOD-123-CPU/OpenInterview/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/OpenInterview/actions/workflows/ci.yml)

### HanBayes · Interpretable ML experiment

从 Multinomial NB 基线逐步加入互信息特征权重、冗余抑制与稀疏类别条件依赖修正。冻结配置、最终结果、McNemar 与 paired bootstrap 组成证据链；CI 另外锁定 tied-score AUC、exact McNemar、seeded bootstrap 等统计原语，并检查已发布结果与 frozen config 的 artifact contract。

**Python · Sparse linear algebra · Statistical testing**

[算法说明](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) · [冻结配置](https://github.com/GOOD-123-CPU/hanbayes/blob/main/configs/frozen.json) · [结果](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv)

[![HanBayes CI](https://github.com/GOOD-123-CPU/hanbayes/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/hanbayes/actions/workflows/ci.yml)

### VoxFrontier · Reproducible analytics pipeline

用合成直播数据连接 DEA、贡献归因、Double ML 与反事实模拟。每次运行写入输入和结果表 SHA-256、随机种子、依赖环境与摘要，使“结果是否为同一次运行”可以被重新核验。

**Python · Causal inference · Reproducible research**

[方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [Manifest 实现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/src/voxfrontier/utils/manifest.py) · [仓库](https://github.com/GOOD-123-CPU/voxFrontier)

## Engineering principles

| 关注点 | 公开项目里的实现 |
| :--- | :--- |
| **Deterministic core** | Itinera 的语义约束与候选 ID 绑定；Investment Committee 用代码计算的量化指标覆盖模型返回值并由单测锁定 |
| **Model output is untrusted** | JSON 形状校验、分数钳制、来源限制、低置信度拒答/兜底 |
| **Failure-aware orchestration** | 有界并发、组件级降级、OpenInterview 原子 task lease、缓存与流式错误处理 |
| **Verification** | Type checking、unit/statistical tests、production build、secret/dependency scanning、跨 Python/OS CI |
| **Reproducibility** | HanBayes frozen config / raw metrics；VoxFrontier run manifest / SHA-256 |

CI 证明的是对应提交的自动检查结果，不等同于业务效果、模型质量或生产可靠性；这些结论需要各自的 benchmark、集成测试与真实运行证据。

## More projects

- **Knowledge & RAG:** [LexAtlas](https://github.com/GOOD-123-CPU/LexAtlas) · [NutriMentor](https://github.com/GOOD-123-CPU/nutrimentor)
- **AI + business:** [Retail Audit Agent](https://github.com/GOOD-123-CPU/retail-audit-agent) · [AlphaDebate / FinSightPro](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) · [Investment Committee](https://github.com/GOOD-123-CPU/investment-committee)
- **Java business systems:** [Green Certificate Trading](https://github.com/GOOD-123-CPU/green-cert-trading) · [Gavel](https://github.com/GOOD-123-CPU/gavel)
- **Research tooling & writing:** [Research Figure Workbench](https://github.com/GOOD-123-CPU/research-figure-workbench) · [Green Finance Literature Review](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review)

完整仓库、源码入口与验证范围见 [PROJECTS.md](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/PROJECTS.md)。方法、实现或复现问题欢迎在对应仓库 Issue 中讨论。
