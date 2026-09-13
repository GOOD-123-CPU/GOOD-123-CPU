# David Zhu

**Data Science and Big Data Technology · 数据科学与大数据技术**

I build projects that connect **statistical modeling, causal inference, information retrieval, and visual applications** — carrying each one all the way from problem definition to reproducible evidence.

你好，我是 David Zhu。这个主页整理了我在机器学习、统计与因果分析、中文 NLP、RAG 检索、数据可视化方向的实践。相比只展示代码，我更关注一条完整链路：

**问题定义 → 数据处理 → 模型/方法 → 评估证据 → 可运行应用 → 文档复现**

[![Repos](https://img.shields.io/badge/repositories-16-0F6E56?style=flat-square)](https://github.com/GOOD-123-CPU?tab=repositories)
[![Focus](https://img.shields.io/badge/focus-causal%20inference%20%C2%B7%20RAG%20%C2%B7%20visualization-534AB7?style=flat-square)](#能力矩阵)
[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://github.com/GOOD-123-CPU/hanbayes)
[![Vue](https://img.shields.io/badge/-Vue%203-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)](https://github.com/GOOD-123-CPU/screenweaver)

---

## 代表项目

| 项目 | 研究问题 / 应用场景 | 方法与实现 | 推荐入口 |
| :--- | :--- | :--- | :--- |
| **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** | 中文情感分类：模型改进 + 预测可解释 | 朴素贝叶斯、字符 n-gram、稀疏特征加权、可复现评测 | [结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [算法](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) |
| **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** | 直播效率测度与因果效应估计 | DEA、贡献归因、Double ML、反事实模拟 | [方法](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md) |
| **[MediRAG](https://github.com/GOOD-123-CPU/medirag-open)** | 医疗文档检索与来源可追溯问答 | 多路召回、RRF 融合、重排序、Milvus | [中文 README](https://github.com/GOOD-123-CPU/medirag-open) |
| **[LexAtlas](https://github.com/GOOD-123-CPU/LexAtlas)** | 法律知识检索与智能问答平台 | Spring Boot、Vue 3、Milvus、LLM 编排 | [项目主页](https://github.com/GOOD-123-CPU/LexAtlas) |
| **[ScreenWeaver](https://github.com/GOOD-123-CPU/screenweaver)** | 用配置驱动数据、图表与大屏布局 | TypeScript、Vue 3、ECharts、HTTP / WebSocket | [示例配置](https://github.com/GOOD-123-CPU/screenweaver/blob/main/public/configs/city-ops.json) |
| **[AlphaDebate / FinSightPro](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch)** | 结构化行情数据与多角色研究报告生成 | Python、AkShare、多智能体辩论 | [项目主页](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) |

---

## 从结果出发

我倾向于先给数字，再讲方法。下面两个项目都保留了可核对的原始结果文件。

### HanBayes · 可解释中文情感分类

模型对比基准（ChnSentiCorp，清洗后测试集 1,178 条）：

| 模型 | Accuracy | Macro-F1 | AUC |
| :--- | ---: | ---: | ---: |
| StandardNB 基线 | 0.7793 | 0.7786 | 0.8505 |
| **SDFWNB（本文方法）** | **0.8073** | **0.8065** | **0.8867** |

> Accuracy 提升 **+2.80pp**，Macro-F1 提升 **+0.0279**。数值取自仓库已提交的结果文件，非实时运行结果。

[![HanBayes 模型对比图](https://raw.githubusercontent.com/GOOD-123-CPU/hanbayes/main/docs/assets/benchmark.png)](https://github.com/GOOD-123-CPU/hanbayes)

[冻结配置](https://github.com/GOOD-123-CPU/hanbayes/blob/main/configs/frozen.json) · [完整结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [复现说明](https://github.com/GOOD-123-CPU/hanbayes)

### VoxFrontier · 效率分析与因果估计

从合成数据出发，串联效率测度 → 贡献归因 → 因果估计 → 情景模拟，附带完整方法说明与可复现流程。

[![VoxFrontier 合成数据分析总览](https://raw.githubusercontent.com/GOOD-123-CPU/voxFrontier/main/figures/dashboard.png)](https://github.com/GOOD-123-CPU/voxFrontier)

> 示例结果用于方法演示，不代表真实平台的实证结论。

[方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [使用与复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md)

---

## 能力矩阵

| 能力方向 | 项目证据 | 常用工具与方法 |
| :--- | :--- | :--- |
| 数据处理与特征工程 | HanBayes、VoxFrontier、Retail Audit Agent | Python、pandas、NumPy、文本清洗、稀疏特征、SQL |
| 机器学习与统计建模 | HanBayes、VoxFrontier | 贝叶斯分类、DEA、Double ML、Bootstrap、模型对比 |
| 检索与 AI 应用 | MediRAG、LexAtlas、NutriMentor | RAG、向量检索、RRF、重排序、LLM 编排 |
| 数据可视化与前端 | ScreenWeaver、VoxFrontier | Vue 3、TypeScript、ECharts、交互式仪表盘 |
| 工程化与复现 | HanBayes、VoxFrontier、OpenInterview | Docker、GitHub Actions、pre-commit、配置冻结、结果文件 |

---

## 更多探索

[智能面试系统 OpenInterview](https://github.com/GOOD-123-CPU/OpenInterview) · [零售审计 Agent](https://github.com/GOOD-123-CPU/retail-audit-agent) · [绿证交易平台](https://github.com/GOOD-123-CPU/green-cert-trading) · [绿色金融文献综述](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review) · [全部公开仓库](https://github.com/GOOD-123-CPU?tab=repositories)

欢迎通过对应项目的 Issues 交流复现问题、方法讨论与改进建议。

---

### About

My field of study is **Data Science and Big Data Technology**. I work on interpretable machine learning, statistical and causal analysis, information retrieval, and data visualization — with a consistent emphasis on reproducible evidence and runnable deliverables.

Start with **HanBayes** for Chinese sentiment classification with reproducible model comparison, or **VoxFrontier** for an efficiency and causal-estimation pipeline. **MediRAG**, **LexAtlas**, and **ScreenWeaver** extend this work into knowledge applications and visual interfaces.
