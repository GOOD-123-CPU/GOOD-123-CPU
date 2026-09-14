# David Zhu

**Software Engineering · AI Applications · Reproducible Data Science**

你好，我是 David Zhu，数据科学与大数据技术方向。我构建检索问答系统、业务工作台和数据可视化工具，关注模块边界、异步资源管理、自动化测试与可复现交付。

I build AI applications and data tools with explicit interfaces, testable components, and reproducible delivery. My projects span Java backends, TypeScript interfaces, and Python research pipelines.

[工程项目](#工程项目) · [设计与实现](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/ENGINEERING.md) · [完整项目目录](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/PROJECTS.md) · [研究结果](#研究结果)

从 **ScreenWeaver** 看可复用引擎，从 **Itinera** 看完整产品流程，从 **MediRAG** 看 Java 后端；**HanBayes** 和 **VoxFrontier** 展示模型实现与实验复现。下面的作品按这些不同能力选择。

## 工程项目

### ScreenWeaver / 配置驱动的可视化引擎

将 JSON 配置、数据源管理与 Vue 渲染分层；通过组件注册表扩展图表，支持 HTTP 轮询和 WebSocket 数据。适合先体验，再阅读实现。

**Vue 3 · TypeScript · ECharts**

[在线演示](https://good-123-cpu.github.io/screenweaver/) · [架构与取舍](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/architecture.md) · [连接与生命周期](https://github.com/GOOD-123-CPU/screenweaver/blob/main/src/engine/useSources.ts)

[![ScreenWeaver CI](https://github.com/GOOD-123-CPU/screenweaver/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/screenweaver/actions/workflows/ci.yml)

### Itinera / AI 行程产品原型

将自然语言需求转换为结构化行程，再呈现为时间线、地图和费用明细。行程解析与兜底逻辑独立为纯函数，模型输出经过字段检查；天气和预订等流程包含演示逻辑。

**Next.js · TypeScript · Prisma · SQLite · Leaflet**

[产品截图与启动](https://github.com/GOOD-123-CPU/itinera#readme) · [行程引擎](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) · [测试](https://github.com/GOOD-123-CPU/itinera/blob/main/tests/itinerary.test.ts)

[![Itinera CI](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/itinera/actions/workflows/ci.yml)

<details>
<summary>查看 Itinera 产品界面</summary>

[![Itinera 行程界面](https://raw.githubusercontent.com/GOOD-123-CPU/itinera/main/docs/screenshots/readme-itinerary.png)](https://github.com/GOOD-123-CPU/itinera)

</details>

### MediRAG / 检索问答系统

以独立组件组织召回、融合、重排序和回答生成。工程阅读重点是 REST/SSE 接口、存储职责、请求追踪与部署依赖。

**Java · Spring Boot · Vue 3 · Milvus · Redis · MinIO**

[系统架构](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) · [检索链路](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md) · [启动与评估边界](https://github.com/GOOD-123-CPU/medirag-open#readme)

[![MediRAG CI](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/medirag-open/actions/workflows/ci.yml)

### Retail Audit Agent / 业务流程工作台

连接资料解析、规则分析、模型解释和报告生成。分析编排限制解释调用的并发数，并保留风险与解释的对应顺序。

**Next.js · React · TypeScript · SQLite / MySQL**

[本地体验](https://github.com/GOOD-123-CPU/retail-audit-agent#readme) · [分析编排源码](https://github.com/GOOD-123-CPU/retail-audit-agent/blob/main/lib/analysis.ts) · [测试与构建](https://github.com/GOOD-123-CPU/retail-audit-agent/blob/main/.github/workflows/ci.yml)

[![Retail Audit CI](https://github.com/GOOD-123-CPU/retail-audit-agent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/GOOD-123-CPU/retail-audit-agent/actions/workflows/ci.yml)

## 工程实践

| 关注点 | 可检查的实现 |
| :--- | :--- |
| 模块与接口 | ScreenWeaver 的配置、数据源和组件注册；MediRAG 的分阶段检索链路 |
| 资源与失败处理 | WebSocket 指数退避、卸载时关闭连接；模型解释的有界并发 |
| 验证与交付 | 配置校验、类型检查、单元测试、应用构建和库构建；工作流见各项目 CI |
| 实验可复现 | HanBayes 冻结配置与结果 CSV；VoxFrontier 合成数据与运行 manifest |

[工程阅读指南](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/ENGINEERING.md) 记录源码入口、实现取舍和待完善的边界。CI 徽章展示工作流状态，性能与业务效果需要各自的评估证据。

## 研究与工具

| 项目 | 解决的问题 | 从这里开始 |
| :--- | :--- | :--- |
| **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** | 中文情感分类：贝叶斯基线、特征加权与可解释预测 | [模型对比结果](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [算法说明](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) |
| **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** | 直播效率分析：DEA、归因、Double ML 与反事实模拟 | [方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [复现指南](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md) |

## 研究结果

<details>
<summary>HanBayes 模型对比与 VoxFrontier 分析图</summary>

### HanBayes · 中文情感分类

仓库已提交的模型对比结果：

| 模型 | Accuracy | Macro-F1 | AUC |
| :--- | ---: | ---: | ---: |
| StandardNB | 0.7793 | 0.7786 | 0.8505 |
| FWNB | 0.8022 | 0.8009 | 0.8770 |
| DFWNB-v2 | 0.8048 | 0.8033 | 0.8822 |
| **SDFWNB** | **0.8073** | **0.8065** | **0.8867** |

SDFWNB 相比 StandardNB，Accuracy 提高 **2.80 个百分点**，Macro-F1 提高 **0.0279**。这些是仓库保存的实验结果，不是实时评测，也不代表在其他数据集上的表现。

[![HanBayes 模型对比图](https://raw.githubusercontent.com/GOOD-123-CPU/hanbayes/main/docs/assets/benchmark.png)](https://github.com/GOOD-123-CPU/hanbayes)

[原始结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [冻结配置](https://github.com/GOOD-123-CPU/hanbayes/blob/main/configs/frozen.json) · [复现入口](https://github.com/GOOD-123-CPU/hanbayes#readme)

### VoxFrontier · 效率分析与因果估计

从合成数据出发，连接 **效率测度 → 贡献归因 → 因果估计 → 情景模拟**，保留方法说明、结果表与运行记录。

[![VoxFrontier 合成数据分析总览](https://raw.githubusercontent.com/GOOD-123-CPU/voxFrontier/main/figures/dashboard.png)](https://github.com/GOOD-123-CPU/voxFrontier)

示例用于展示分析方法，不代表真实平台的实证结论；因果解释依赖识别假设，情景模拟也不等于经过验证的干预效果。

[方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [使用与复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md)

</details>

## 更多探索

[完整项目目录](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/PROJECTS.md) 按工程产品、研究方法、领域 AI 与工具组织全部公开仓库，每个项目都附实现入口和验证范围。

- **知识与 AI 应用**：[LexAtlas](https://github.com/GOOD-123-CPU/LexAtlas) · [NutriMentor](https://github.com/GOOD-123-CPU/nutrimentor) · [OpenInterview](https://github.com/GOOD-123-CPU/OpenInterview)
- **金融与业务系统**：[AlphaDebate / FinSightPro](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) · [Investment Committee](https://github.com/GOOD-123-CPU/investment-committee) · [绿证交易](https://github.com/GOOD-123-CPU/green-cert-trading) · [Gavel 拍卖](https://github.com/GOOD-123-CPU/gavel)
- **科研工具与写作**：[Research Figure Workbench](https://github.com/GOOD-123-CPU/research-figure-workbench) · [绿色金融综述](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review)

## 交流

欢迎通过对应项目的 **Issues** 讨论方法、反馈问题或交流复现结果。项目的安装步骤、依赖和适用边界以各仓库文档为准。
