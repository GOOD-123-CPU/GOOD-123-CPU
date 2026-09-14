# Project Directory

Review date: 2026-09-14. 16 public repositories.

[Profile](https://github.com/GOOD-123-CPU) | [Engineering notes](ENGINEERING.md)

The review covers repository structure, README content, selected implementation files,
and workflow records. It is not a full code audit or an end-to-end run of every app.

Entries describe the review snapshot. Follow each repository for current status.

## 工程与产品

| 项目与入口 | 实现重点 | 验证与边界 |
| --- | --- | --- |
| [screenweaver](https://github.com/GOOD-123-CPU/screenweaver) · [架构](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/architecture.md) | 配置驱动可视化引擎；数据源、组件注册与渲染分层。 | 配置校验、测试、应用与库构建 CI |
| [itinera](https://github.com/GOOD-123-CPU/itinera) · [行程引擎](https://github.com/GOOD-123-CPU/itinera/blob/main/src/lib/itinerary.ts) | AI 行程产品原型；结构化输出解析、确定性兜底、地图与订单模拟。 | 行程、LLM、密码与限流测试；构建 CI |
| [medirag-open](https://github.com/GOOD-123-CPU/medirag-open) · [系统架构](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/ARCHITECTURE.md) | Java 医疗知识问答；多阶段检索、来源引用与多服务部署。 | 后端验证、前端构建与扫描 CI；离线词法评估不等于完整 RAG 评估 |
| [retail-audit-agent](https://github.com/GOOD-123-CPU/retail-audit-agent) · [分析编排](https://github.com/GOOD-123-CPU/retail-audit-agent/blob/main/lib/analysis.ts) | 零售审计演示工作台；规则分析、受限并发解释与报告编排。 | 类型检查、单测与构建 CI；哈希伪向量不代表语义检索 |
| [OpenInterview](https://github.com/GOOD-123-CPU/OpenInterview) · [架构](https://github.com/GOOD-123-CPU/OpenInterview/blob/main/docs/architecture.md) | 语音面试应用；简历、出题、转录、异步报告与事件通知。 | pytest 与 CI；自动报告应由人工复核 |
| [green-cert-trading](https://github.com/GOOD-123-CPU/green-cert-trading) · [启动与目录](https://github.com/GOOD-123-CPU/green-cert-trading/blob/main/README.md) | 绿证交易学习系统；商城、拼团、库存与管理端。 | 后端测试与前端构建 CI；不代表真实交易结算能力 |
| [gavel](https://github.com/GOOD-123-CPU/gavel) · [测试样例](https://github.com/GOOD-123-CPU/gavel/blob/main/server/src/test/java/com/gavel/controller/PasswordVerificationTest.java) | 拍卖学习系统；Spring Boot、Vue 2 管理端与 HTML 门户。 | CI 与安全行为测试；并发竞价及持久化仍需集成验证 |

## 研究与方法

| 项目与入口 | 实现重点 | 验证与边界 |
| --- | --- | --- |
| [hanbayes](https://github.com/GOOD-123-CPU/hanbayes) · [Python API](https://github.com/GOOD-123-CPU/hanbayes/blob/main/src/hanbayes/analyzer.py) | 可解释贝叶斯分类包；共享稀疏特征、模型对比与冻结实验配置。 | 测试与 CI；已提交模型结果、Bootstrap 和 McNemar 表 |
| [voxFrontier](https://github.com/GOOD-123-CPU/voxFrontier) · [复现记录](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/src/voxfrontier/utils/manifest.py) | 效率与因果分析流水线；DEA、归因、DML、情景模拟及结果哈希。 | 测试与 CI；公开结果为合成数据演示 |
| [green-finance-high-quality-development-review](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review) · [论文](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review/blob/main/paper.md) | 绿色金融文献综述；提供 Markdown、PDF、Word 与引用元数据。 | 研究写作成果；不是软件项目，不以构建状态评价 |

## 领域 AI 与工具

| 项目与入口 | 实现重点 | 验证与边界 |
| --- | --- | --- |
| [LexAtlas](https://github.com/GOOD-123-CPU/LexAtlas) · [架构](https://github.com/GOOD-123-CPU/LexAtlas/blob/main/docs/ARCHITECTURE.md) | 法律知识检索应用；RAG、文档入库、缓存与管理功能。 | Java 与 Vue 测试、构建 CI；领域效果需独立评估 |
| [nutrimentor](https://github.com/GOOD-123-CPU/nutrimentor) · [评估实现](https://github.com/GOOD-123-CPU/nutrimentor/blob/main/src/nutrimentor/evaluation.py) | Python 营养教学平台；混合检索、教学人格、会话与诊断 CLI。 | 单测与 CI；recall@K 字段实际按查询命中比例计算 |
| [AlphaDebate-FinResearch](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) · [编排器](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch/blob/main/finsight/services/orchestrator.py) | FinSightPro：Python 多角色辩论与研报生成，包含数据和模型编排。 | 编排、问答与路由测试 CI；模型评审分数不代表投资效果 |
| [investment-committee](https://github.com/GOOD-123-CPU/investment-committee) · [研究流水线](https://github.com/GOOD-123-CPU/investment-committee/blob/main/src/lib/pipeline/runner.ts) | Next.js 投研终端原型；市场数据、智能体、辩论、投票与报告。 | 本次目录检查未发现测试套件或应用 CI；优先补交付验证 |
| [research-figure-workbench](https://github.com/GOOD-123-CPU/research-figure-workbench) · [预检脚本](https://github.com/GOOD-123-CPU/research-figure-workbench/blob/main/scripts/preflight_figure.py) | 科研制图工作流与 Python 检查脚本；支持图表文件预检。 | 提供 smoke render；本次未发现 CI，文件预检不等于视觉审核 |

## 主页与导航

| 项目与入口 | 实现重点 | 验证与边界 |
| --- | --- | --- |
| [GOOD-123-CPU](https://github.com/GOOD-123-CPU/GOOD-123-CPU) · [工程指南](https://github.com/GOOD-123-CPU/GOOD-123-CPU/blob/main/ENGINEERING.md) | 个人工程作品入口、全项目目录与设计阅读指南。 | 目录由结构化清单生成，并通过一致性检查 |

## Maintenance

Edit `projects.json`, then run `python scripts/catalog.py`.
CI runs `python scripts/catalog.py --check` to detect drift and invalid entries.
This check validates the local catalog, not live repository availability or application behavior.
