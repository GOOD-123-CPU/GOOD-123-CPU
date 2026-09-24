# Engineering Notes

[返回主页](https://github.com/GOOD-123-CPU)

这里按工程问题组织项目入口，便于检查实现、理解取舍和复现验证。阅读基准更新至 2026-09-24；源码链接尽量固定到核查版本，工作流链接指向持续更新的记录。

## 1. ScreenWeaver：配置如何变成持续更新的界面

**边界。** 配置描述布局、组件和数据源；引擎将数据源转换为响应式状态；渲染层通过注册表分派组件。业务组件用 key 订阅数据，数据接入方式集中在引擎中。

**资源生命周期。** WebSocket 断开后按指数退避重连，上限 30 秒；成功连接后重置重试计数。HTTP 数据源为每个 source 维护单独的 `AbortController`：上一轮请求未完成时跳过新的轮询，组件卸载时取消在途请求。WebSocket 与轮询定时器也在卸载时统一清理。

**取舍。** 固定设计尺寸并整体等比缩放有利于保留大屏的相对位置，但不同宽高比会留白。声明式配置便于复用，同时需要显式的字段验证和扩展契约。

**当前边界。** HTTP 请求现在会检查 `res.ok`，慢请求不会叠加，并支持在卸载时取消；这些行为有单元测试覆盖。仍未实现显式请求超时策略，WebSocket 指数退避也尚未加入 jitter。真实网络抖动、浏览器切后台与长时间运行场景仍需要单独的集成/端到端验证。

[架构](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/architecture.md) · [核查版本源码](https://github.com/GOOD-123-CPU/screenweaver/blob/5b85c528f7a1c3f65e286adc5405da42bfa6d5ac/src/engine/useSources.ts) · [HTTP 数据源测试](https://github.com/GOOD-123-CPU/screenweaver/blob/5b85c528f7a1c3f65e286adc5405da42bfa6d5ac/tests/engine.spec.ts) · [CI](https://github.com/GOOD-123-CPU/screenweaver/actions/workflows/ci.yml)

CI 执行依赖安装、示例配置校验、单元测试、类型检查与应用构建、库构建。网络中断与真实浏览器场景仍应单独验证。

## 2. Retail Audit Agent：规则与模型调用如何协作

**执行顺序。** 读取规则，计算指标与风险，再为每项风险生成解释，最后构造报告和底稿。规则结果与模型解释分开，便于分别检查业务判定和生成内容。

**并发约束。** `mapWithConcurrency` 使用共享游标分发任务，将结果写回原始索引；`EXPLAIN_CONCURRENCY = 3` 限制一次分析中的解释并发数。结果顺序与风险顺序一致。

**取舍与边界。** 这是单次分析内的并发上限，不是所有请求共享的全局限流。编排层使用 `Promise.all`；如果 worker 抛出未处理异常，整次等待会拒绝，其他已开始任务不会自动取消。高并发部署还需考虑全局配额、取消传播和部分失败策略。

[核查版本源码](https://github.com/GOOD-123-CPU/retail-audit-agent/blob/269ef1bd46e9336cb6a7dca99f430dd331aaaeea/lib/analysis.ts) · [CI](https://github.com/GOOD-123-CPU/retail-audit-agent/actions/workflows/ci.yml) · [运行与功能说明](https://github.com/GOOD-123-CPU/retail-audit-agent#readme)

CI 执行类型检查、单元测试和生产构建。仓库的哈希伪向量模块用于演示，不能作为语义检索效果的证据。

## 3. MediRAG：应用链路与验证范围

**模块划分。** 架构文档将查询改写、双路召回、RRF 融合、重排序和 Prompt 组装划为独立组件。业务数据、向量数据和原始文件分别由 MySQL、Milvus 和 MinIO 承担；Redis 用于缓存与限流。

**交付检查。** CI 分别运行后端 `mvn -B verify` 和前端安装、构建；另有密钥扫描和仅在 PR 上执行的依赖审查。覆盖率与构建产物设置了上传步骤，其中缺失文件采用 `ignore`，因此成功工作流本身不能证明每类产物均存在。

**验证边界。** README 已说明离线检索脚本使用词法信号，不调用完整 Milvus、重排序及生成链路。完整效果评估需要独立标注的查询与相关文档、固定数据版本、检索阶段对比及回答引用检查。

[架构与接口](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) · [评估范围](https://github.com/GOOD-123-CPU/medirag-open#readme) · [CI](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml)

## 4. Itinera：模型输出如何进入产品流程

`src/lib/itinerary.ts` 将行程解析和兜底构造组织为纯函数。解析器读取模型返回的 itinerary JSON 代码块，检查标题、步骤数组、时间等字段；输入失败时返回空结果，由调用方选择后续策略。独立的 `tests/itinerary.test.ts` 提供解析及兜底行为的测试入口。

这体现了把模型输出作为待校验输入的工程边界。字段形状检查仍不等于现实约束验证：时间顺序、实际营业时间、路线可达性和真实预订需要额外数据与业务校验。当前项目明确将天气、预订和部分数据定位为演示。

[行程引擎](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [测试](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts) · [API](https://github.com/GOOD-123-CPU/itinera/blob/main/API.md)

## 5. HanBayes 与 VoxFrontier：研究代码的工程表达

HanBayes 的 `ChineseSentimentAnalyzer` 提供统一训练入口，将共享特征处理与具体模型实现分开，并提供解释接口、冻结配置和实验结果文件。VoxFrontier 的 manifest 写入输入与结果表的 SHA-256、环境信息、随机种子和运行摘要，使结果漂移可以被核查。

这里应区分两种承诺：文件哈希能检查文件是否一致；统计结论是否成立仍取决于数据、方法和实验协议。主页因此同时链接实现、方法说明和原始结果。

[HanBayes API](https://github.com/GOOD-123-CPU/hanbayes/blob/main/src/hanbayes/analyzer.py) · [VoxFrontier manifest](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/src/voxfrontier/utils/manifest.py)

## 可核查的交付记录

以下是核查时已成功完成的工作流记录；它们只证明对应提交的检查结果，不代表未来提交或所有部署环境。

| 项目 | 成功记录 |
| :--- | :--- |
| ScreenWeaver | [CI run 35949190502](https://github.com/GOOD-123-CPU/screenweaver/actions/runs/35949190502)（2026-09-24，含 HTTP 生命周期修复与测试） |
| Retail Audit Agent | [CI run 34741136840](https://github.com/GOOD-123-CPU/retail-audit-agent/actions/runs/34741136840) |
| MediRAG | [CI run 34741206405](https://github.com/GOOD-123-CPU/medirag-open/actions/runs/34741206405) |
| VoxFrontier | [CI run 34740061138](https://github.com/GOOD-123-CPU/voxFrontier/actions/runs/34740061138) |

## 技术交流

全部公开仓库及其阅读入口见 [项目目录](PROJECTS.md)。目录覆盖工程产品、研究分析、领域应用、工具和写作成果；没有应用 CI 的项目会单独注明，不与已通过构建的项目混淆。

讨论实现时，可在对应仓库 Issue 中提供运行环境、复现步骤、预期与实际结果。方法讨论可附数据版本、配置和原始指标，方便核对与复现。
