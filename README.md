# David Zhu

**Data Science and Big Data Technology | 数据科学与大数据技术**

I build data projects that connect **statistical modeling, reproducible evaluation, information retrieval, and visual applications**.

你好，我是 David Zhu，专业是数据科学与大数据技术。这个主页整理了我在机器学习、统计分析、中文 NLP、RAG、数据可视化与业务分析方向的项目实践。相比只展示代码，我更关注一条完整链路：**问题定义 -> 数据处理 -> 模型/方法 -> 评估证据 -> 可运行应用 -> 文档复现**。

[Machine Learning](https://github.com/GOOD-123-CPU/hanbayes) · [Statistical Analysis](https://github.com/GOOD-123-CPU/voxFrontier) · [RAG / Retrieval](https://github.com/GOOD-123-CPU/medirag-open) · [Data Visualization](https://github.com/GOOD-123-CPU/screenweaver) · [All Repositories](https://github.com/GOOD-123-CPU?tab=repositories)

## 代表项目

| 项目 | 研究问题 / 应用场景 | 方法与实现 | 推荐入口 |
| :--- | :--- | :--- | :--- |
| **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** | 中文情感分类：比较模型改进，并解释预测依据 | 朴素贝叶斯、字符 n-gram、稀疏矩阵、特征加权、可复现实验 | [结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [算法](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) |
| **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** | 使用合成数据探索声音特征与直播效率的关系 | DEA、贡献归因、Double Machine Learning、反事实模拟 | [方法](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md) |
| **[MediRAG](https://github.com/GOOD-123-CPU/medirag-open)** | 医疗知识文档的检索与来源可追溯问答 | 多路召回、RRF、重排序、Milvus、Spring Boot、Vue | [中文 README](https://github.com/GOOD-123-CPU/medirag-open) |
| **[ScreenWeaver](https://github.com/GOOD-123-CPU/screenweaver)** | 用配置组织数据、图表与大屏布局 | TypeScript、Vue、ECharts、HTTP / WebSocket 数据接入 | [示例配置](https://github.com/GOOD-123-CPU/screenweaver/blob/main/public/configs/city-ops.json) · [数据接入](https://github.com/GOOD-123-CPU/screenweaver/blob/main/docs/data-integration.md) |
| **[Retail Audit Agent](https://github.com/GOOD-123-CPU/retail-audit-agent)** | 零售资料分析、规则风险识别与审计工作流演示 | 文档解析、规则评分、LLM 解释、Next.js、SQL 存储 | [项目主页](https://github.com/GOOD-123-CPU/retail-audit-agent) |
| **[AlphaDebate / FinSightPro](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch)** | 结构化行情数据与多角色金融研究报告生成 | Python、AkShare、多智能体辩论、流式输出 | [项目主页](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) |

## 从结果开始

### HanBayes · 可解释中文情感分类

HanBayes 比较多种贝叶斯文本分类模型，并保留数据清洗、冻结配置、预测解释和结果复现入口。仓库保存的 ChnSentiCorp 最终测试结果如下；数值来自已提交结果文件，不是实时运行状态，也不代表其他数据集上的效果。

| 模型 | Accuracy | Macro-F1 | AUC |
| :--- | ---: | ---: | ---: |
| StandardNB 基线 | 0.7793 | 0.7786 | 0.8505 |
| SDFWNB | 0.8073 | 0.8065 | 0.8867 |

清洗后测试集为 1,178 条；最终训练使用清洗后的 train + dev。Accuracy 提升约 2.80 个百分点，Macro-F1 提升约 0.0279。

[冻结配置](https://github.com/GOOD-123-CPU/hanbayes/blob/main/configs/frozen.json) · [完整结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [复现说明](https://github.com/GOOD-123-CPU/hanbayes)

[![HanBayes 模型对比图](https://raw.githubusercontent.com/GOOD-123-CPU/hanbayes/main/docs/assets/benchmark.png)](https://github.com/GOOD-123-CPU/hanbayes)

### VoxFrontier · 效率分析与因果估计实验

VoxFrontier 从合成数据出发，串联效率测度、贡献归因、因果估计与情景模拟。项目保留方法说明、使用指南与结果文件；示例结果用于方法演示，不代表真实平台的实证结论。

[![VoxFrontier 合成数据分析总览](https://raw.githubusercontent.com/GOOD-123-CPU/voxFrontier/main/figures/dashboard.png)](https://github.com/GOOD-123-CPU/voxFrontier)

[方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [使用与复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md)

## 能力矩阵

| 能力方向 | 项目证据 | 常用工具与方法 |
| :--- | :--- | :--- |
| 数据处理与特征工程 | HanBayes、VoxFrontier、Retail Audit Agent | Python、pandas、NumPy、文本清洗、稀疏特征、SQL |
| 机器学习与统计建模 | HanBayes、VoxFrontier | 贝叶斯分类、DEA、DML、Bootstrap、模型对比 |
| 检索与 AI 应用 | MediRAG、LexAtlas、Retail Audit Agent | RAG、向量检索、RRF、重排序、LLM 应用编排 |
| 数据可视化与前端应用 | ScreenWeaver、VoxFrontier | Vue、TypeScript、ECharts、交互式仪表盘 |
| 工程化与复现 | HanBayes、MediRAG、AlphaDebate | Docker、GitHub Actions、配置文件、README、结果文件 |

## 更多探索

[绿色金融文献综述](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review) · [绿证交易平台](https://github.com/GOOD-123-CPU/green-cert-trading) · [法律知识检索](https://github.com/GOOD-123-CPU/LexAtlas) · [全部公开仓库](https://github.com/GOOD-123-CPU?tab=repositories)

欢迎通过对应项目的 Issues 交流复现问题、方法讨论和改进建议。

---

### About

My field of study is **Data Science and Big Data Technology**. My projects explore interpretable machine learning, statistical analysis, information retrieval, data visualization, and practical AI applications.

Start with **HanBayes** for Chinese sentiment classification and reproducible model comparison, or **VoxFrontier** for an efficiency and causal-estimation pipeline using synthetic data. **MediRAG**, **ScreenWeaver**, and related projects extend this work into knowledge applications and visual interfaces.
