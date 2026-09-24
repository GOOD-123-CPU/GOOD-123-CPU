# Engineering Notes

[返回主页](https://github.com/GOOD-123-CPU)

这里按工程问题组织项目入口，便于检查实现、理解取舍和复现验证。阅读基准更新至 **2026-09-24**。本文只描述已经能从公开源码、测试或工作流中核查的事实；CI 成功不等于业务效果、模型质量或生产可靠性。

## 1. ScreenWeaver：配置如何变成持续更新的界面

**边界。** 配置描述布局、组件和数据源；引擎将数据源转换为响应式状态；渲染层通过注册表分派组件。业务组件用 key 订阅数据，数据接入方式集中在引擎中。

**资源生命周期。** WebSocket 断开后按指数退避重连，上限 30 秒；成功连接后重置重试计数。HTTP 数据源为每个 source 维护独立的 `AbortController`：上一轮请求未完成时跳过新的轮询，组件卸载时取消在途请求。HTTP 非 2xx 响应不会被写入业务状态。

**验证。** HTTP 状态码、headers 与 path 提取已有单元测试；配置校验、单测、类型检查、应用构建和库构建进入 CI。

**仍未证明。** 显式请求超时策略、WebSocket jitter、浏览器切后台、真实网络抖动和长时间运行仍需集成或端到端测试。

[架构](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/architecture.md) · [数据源实现](https://github.com/GOOD-123-CPU/screenweaver/blob/main/src/engine/useSources.ts) · [测试](https://github.com/GOOD-123-CPU/screenweaver/blob/main/tests/engine.spec.ts)

## 2. Itinera：模型输出怎样才能进入可执行产品流程

`src/lib/itinerary.ts` 不再只回答“JSON 形状是否正确”。结构化输出还要通过确定性语义检查：

- 日期必须是合法日历日期；
- 每个 step 的结束时间必须晚于开始时间；
- 相邻 step 不得发生时间重叠；
- 经纬度必须处于合法范围；
- 模型返回的 `venueId` / `restaurantId` 必须来自本轮数据库检索候选。

真正创建 reservation 时，服务端重新按 ID 查找本轮候选并使用数据库中的 canonical name，而不是信任模型生成的地点名称。换言之，**模型可以提出计划，但可执行动作必须重新绑定到服务端事实源**。语义检查失败时不会把该结构直接带入业务动作，而是进入已有 fallback 路径。

**仍未证明。** 当前校验可以发现内部时间冲突，却不能证明现实世界的营业时间、实时交通、路线可达性、天气和真实库存/预订状态。

[行程引擎](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [Agent route](https://github.com/GOOD-123-CPU/itinera/blob/main/src/app/api/agent/route.ts) · [测试](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts)

## 3. MediRAG：RAG 评估必须先定义证据等级

**应用链路。** Query 改写、双路召回、RRF、重排序、置信度判断、Prompt 组装、SSE 生成和安全兜底为独立阶段。MySQL、Milvus、MinIO 与 Redis 承担不同存储与运行职责。

**评估契约。** `evaluation/eval_retrieval.py` 现在强制区分两类输入：

1. 每条 query 都有独立 `relevant_doc_ids` 时，才输出真正基于相关文档集合的 **Recall@K / MRR@K**；
2. 没有 qrels 的旧病例只输出 **proxy_hit_rate@K / proxy_mrr@K**，并在结果中标记 `heuristic_keyword_proxy`。

混用有标注和无标注 case 会直接报错。CI 内的合成 qrels fixture 只验证指标公式和契约，不被描述成医疗检索 benchmark。当前公开的 11 科室病例与样例知识库也不被包装成人工标注 ground truth。

**交付与供应链检查。** CI 执行后端 Maven verify、前端类型/构建、Gitleaks、评估单测/合成 sanity benchmark，以及不依赖 GitHub Dependency Graph 的前端高危 `npm audit`。引入 audit 后实际发现并刷新了 Axios/form-data/lodash/nanoid/picomatch/postcss 等锁文件依赖。GitHub Dependency Review 在 Dependency Graph 未启用时仅作为 advisory，不冒充有效门禁。

**仍未证明。** 完整 RAG 效果仍需要固定真实知识库版本和独立 qrels，分别评估 vector/keyword recall、RRF、reranker、引用对齐和生成事实性；医疗适用性需要更高等级的领域验证。

[RAG 链路](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md) · [评估器](https://github.com/GOOD-123-CPU/medirag-open/blob/main/evaluation/eval_retrieval.py) · [评估测试](https://github.com/GOOD-123-CPU/medirag-open/blob/main/evaluation/test_eval_retrieval.py)

## 4. OpenInterview：业务状态与 worker 执行所有权分开

状态扫描本身不能保证多 worker 幂等：两个进程可能同时看到同一个 `NOT_STARTED` / `COMPLETED` 记录，然后重复执行 LLM 或 PDF 工作。

现在额外使用 SQLite `task_leases` 表保存 `(task_type, entity_id, owner, lease_until)`。认领通过 `BEGIN IMMEDIATE` 事务完成：

- 同一实体、同一任务同时只能有一个 owner；
- 非 owner 不能释放别人的 lease；
- 正常完成或失败都会主动释放；
- worker 崩溃后，过期 lease 可以被其他进程重新认领；
- 业务状态机继续描述产品状态，lease 只描述执行所有权。

CI 在 Python 3.10 / 3.11 / 3.12 上运行，最终验证记录中为 **62 passed**；新增测试覆盖互斥认领、owner release、lease renew 和 expiry recovery。

**仍未证明。** 当前 lease 默认有固定 TTL，而不是持续 heartbeat；如果单次外部调用超过 lease 时间，仍可能发生重执行。因此外部副作用仍应保持幂等，生产规模更大时可进一步引入队列、幂等 key 或 durable outbox。

[架构与 ADR](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/docs/architecture.md) · [Task lease](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/app/services/task_lease.py) · [服务测试](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/app/tests/test_services.py)

## 5. Investment Committee：LLM 解释不能改写确定性数字

该项目的核心不是“智能体数量”，而是区分**确定性市场/量化事实**和**模型解释**。Quant Agent 可以解释 valuation、momentum 等结果，但模型返回后，权威量化字段会由代码计算值重新覆盖。

2026-09-24 新增 Bun 单测锁定：

- rating 阈值；
- 缺失维度重新归一化；
- Very High risk veto；
- risk penalty 上限；
- position sizing 与 confidence adjustment；
- snapshot/live PE、PB 的数据优先级；
- RSI、波动率与 52 周位置等指标边界。

测试第一次运行实际发现：最新 quote 高于 K-line 窗口最高收盘价时，`pos52w` 可超过 100。实现随后把该语义指标钳制到 0–100，重新运行 CI 后通过。这里的价值不是“测试数量”，而是自动门禁确实发现了一个之前隐藏的业务边界 bug。

**仍未证明。** Bull/Bear debate、Risk Review、CIO synthesis 是工作流设计，不是“多智能体一定比单智能体更准确”的证据。真正比较需要固定数据集，对 single-agent / parallel / debate / debate+review 的事实错误、无依据数字、风险覆盖、矛盾率、延迟和 token 成本做实验。

[Agent/量化流水线](https://github.com/GOOD-123-CPU/investment-committee/blob/main/src/lib/pipeline/agents.ts) · [评分核心](https://github.com/GOOD-123-CPU/investment-committee/blob/main/src/lib/pipeline/scoring.ts) · [确定性测试](https://github.com/GOOD-123-CPU/investment-committee/blob/main/tests/deterministic-core.test.ts)

## 6. HanBayes：研究结果和“可复现”不是同一个词

HanBayes 已有 frozen config、最终指标、McNemar 表和 paired bootstrap 表。新增的验证进一步分成两层：

**统计实现测试。** 单测覆盖 tied-score AUC、perfect separation、exact McNemar 的已知概率，以及 seeded paired bootstrap 的确定性。

**Published artifact contract。** `scripts/verify_published_results.py` 不重新训练模型，而是检查仓库里已经提交的证据是否互相一致，包括：

- `configs/frozen.json` 与打包配置是否一致；
- 模型集合和顺序是否符合冻结实验；
- 指标是否落在合法区间；
- McNemar discordant pair 是否等于 b+c，显著性 flag 是否与 p-value 一致；
- bootstrap 的 seed / resample count 是否来自 frozen config；
- CI 区间、均值和 `ci_excludes_zero` 是否自洽。

这只能证明**已发布 artifact 内部一致**，不能替代从原始数据重新执行 `python scripts/run_pipeline.py --final` 的独立复现。

[算法说明](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) · [统计实现](https://github.com/GOOD-123-CPU/hanbayes/blob/main/src/hanbayes/evaluation.py) · [artifact verifier](https://github.com/GOOD-123-CPU/hanbayes/blob/main/scripts/verify_published_results.py)

## 7. 其他证据链

**Retail Audit Agent。** 规则判定与模型解释分离；单次分析使用有界并发，结果顺序稳定。当前并发限制是单请求级，不等于全局配额；worker 未处理异常仍可能导致整次 `Promise.all` 拒绝。

[分析编排](https://github.com/GOOD-123-CPU/retail-audit-agent/blob/main/lib/analysis.ts)

**VoxFrontier。** run manifest 写入输入/结果 SHA-256、环境、随机种子和摘要，可以核对“是不是同一批文件/同一运行环境”。哈希一致不证明因果识别成立；公开结果仍是合成数据演示。

[Manifest](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/src/voxfrontier/utils/manifest.py)

**LexAtlas。** RAG 流水线的 fallback 判断现在会同步持久化到 `law_message.isFallback`，不再出现 SSE/retrieval log 显示 fallback、数据库却永远写 0 的不一致；修复通过受保护分支 PR 与 CI 后合并。

[RagPipeline](https://github.com/GOOD-123-CPU/LexAtlas/blob/main/src/main/java/com/lexatlas/service/rag/RagPipeline.java)

## 可核查的交付记录

以下记录只证明对应提交/PR 的自动检查状态，不代表所有部署环境，也不替代真实业务或模型效果验证。

| 项目 | 成功记录 | 本轮主要证据 |
| :--- | :--- | :--- |
| ScreenWeaver | [CI 35949190502](https://github.com/GOOD-123-CPU/screenweaver/actions/runs/35949190502) | HTTP 生命周期修复与测试 |
| Itinera | [CI 35950603865](https://github.com/GOOD-123-CPU/itinera/actions/runs/35950603865) | 语义行程约束与 canonical action binding |
| MediRAG | [CI 35950830905](https://github.com/GOOD-123-CPU/medirag-open/actions/runs/35950830905) | label-aware evaluation、依赖审计、构建/扫描 |
| OpenInterview | [CI 35950927142](https://github.com/GOOD-123-CPU/OpenInterview/actions/runs/35950927142) | 62 tests、Python matrix、task lease |
| Investment Committee | [CI 35950863817](https://github.com/GOOD-123-CPU/investment-committee/actions/runs/35950863817) | deterministic-core tests + production build |
| HanBayes | [CI 35950628672](https://github.com/GOOD-123-CPU/hanbayes/actions/runs/35950628672) | statistical primitives + artifact contract |
| LexAtlas | [PR CI 35949238482](https://github.com/GOOD-123-CPU/LexAtlas/actions/runs/35949238482) | fallback persistence test |
| Retail Audit Agent | [CI 34741136840](https://github.com/GOOD-123-CPU/retail-audit-agent/actions/runs/34741136840) | type/test/build |
| VoxFrontier | [CI 34740061138](https://github.com/GOOD-123-CPU/voxFrontier/actions/runs/34740061138) | reproducible pipeline checks |

## 技术交流

全部公开仓库及其阅读入口见 [项目目录](PROJECTS.md)。目录覆盖工程产品、研究分析、领域应用、工具和写作成果；验证范围会明确写出，避免把 CI、合成 sanity test、artifact consistency 或 demo 行为描述成它们并不能证明的更强结论。

讨论实现时，可在对应仓库 Issue 中提供运行环境、复现步骤、预期与实际结果。方法讨论可附数据版本、配置和原始指标，方便核对与复现。
