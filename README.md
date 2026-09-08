# David Zhu

**数据科学与大数据技术 · Data Science and Big Data Technology**

你好，我是 David Zhu，专业是数据科学与大数据技术。这里记录我在统计建模、中文自然语言处理、数据可视化与 AI 应用上的项目实践。

我关注从数据处理、建模与评估，到可解释结果和可运行应用的完整过程。

[机器学习](https://github.com/GOOD-123-CPU/hanbayes) · [统计分析](https://github.com/GOOD-123-CPU/voxFrontier) · [知识检索](https://github.com/GOOD-123-CPU/medirag-open) · [数据可视化](https://github.com/GOOD-123-CPU/screenweaver)

## 代表项目

| 项目 | 研究问题 / 应用场景 | 方法与实现 |
| :--- | :--- | :--- |
| **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** | 中文情感分类：比较模型改进，并解释预测依据 | 朴素贝叶斯、字符 n-gram、稀疏矩阵、特征加权、可复现实验 |
| **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** | 使用合成数据探索声音特征与直播效率的关系 | DEA、贡献归因、Double Machine Learning、反事实模拟 |
| **[MediRAG](https://github.com/GOOD-123-CPU/medirag-open)** | 医疗知识文档的检索与来源可追溯问答 | 多路召回、RRF、重排序、Milvus、Spring Boot、Vue |
| **[ScreenWeaver](https://github.com/GOOD-123-CPU/screenweaver)** | 用配置组织数据、图表与大屏布局 | TypeScript、Vue、ECharts、HTTP / WebSocket 数据接入 |
| **[Retail Audit Agent](https://github.com/GOOD-123-CPU/retail-audit-agent)** | 零售资料分析、规则风险识别与审计工作流演示 | 文档解析、规则评分、LLM 解释、Next.js、SQL 存储 |
| **[AlphaDebate / FinSightPro](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch)** | 结构化行情数据与多角色金融研究报告生成 | Python、AkShare、多智能体辩论、流式输出 |

## 按兴趣浏览

- **机器学习与 NLP**：从 HanBayes 的模型对比、稀疏特征和预测解释开始。
- **统计研究与因果推断**：从 VoxFrontier 的方法假设、合成数据和复现流程开始。
- **数据应用与工程**：从 MediRAG 的检索链路、ScreenWeaver 的数据展示和业务分析项目开始。

## 从实验结果开始

### HanBayes · 可解释中文情感分类

比较四种贝叶斯模型，提供数据清洗、冻结配置、预测解释和结果复现入口。

仓库保存的 ChnSentiCorp 最终测试结果如下。数值来自已提交结果文件，不是实时运行状态，也不代表其他数据集上的效果。

| 模型 | Accuracy | Macro-F1 | AUC |
| :--- | ---: | ---: | ---: |
| StandardNB 基线 | 0.7793 | 0.7786 | 0.8505 |
| SDFWNB | 0.8073 | 0.8065 | 0.8867 |

[冻结配置](https://github.com/GOOD-123-CPU/hanbayes/blob/main/configs/frozen.json) · [完整结果 CSV](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv)

清洗后测试集为 1,178 条；最终训练使用清洗后的 train + dev。Accuracy 提升约 2.80 个百分点，Macro-F1 提升约 0.0279。复现入口见项目 README。

[![HanBayes 模型对比图](https://raw.githubusercontent.com/GOOD-123-CPU/hanbayes/main/docs/assets/benchmark.png)](https://github.com/GOOD-123-CPU/hanbayes)

[结果与评估协议](https://github.com/GOOD-123-CPU/hanbayes#results) · [算法说明](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) · [实验结果文件](https://github.com/GOOD-123-CPU/hanbayes/tree/main/results)

### VoxFrontier · 效率分析与因果估计实验

从合成数据出发，串联效率测度、归因、因果估计与情景模拟。示例结果用于方法演示，不代表真实平台的实证结论。

[![VoxFrontier 合成数据分析总览](https://raw.githubusercontent.com/GOOD-123-CPU/voxFrontier/main/figures/dashboard.png)](https://github.com/GOOD-123-CPU/voxFrontier)

[方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [使用与复现](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md)

## 项目中使用的技术

| 方向 | 技术与方法 |
| :--- | :--- |
| 数据处理与建模 | Python、NumPy、pandas、SciPy、稀疏特征、贝叶斯分类 |
| 统计分析与评估 | DEA、DML、Bootstrap、模型对比与可复现实验 |
| 检索与 AI 应用 | RAG、向量检索、重排序、LLM 应用编排 |
| 数据展示与工程 | SQL、Java / Spring Boot、TypeScript、Vue、ECharts、Docker、GitHub Actions |

## 更多探索

[绿色金融文献综述](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review) · [绿证交易平台](https://github.com/GOOD-123-CPU/green-cert-trading) · [法律知识检索](https://github.com/GOOD-123-CPU/LexAtlas) · [全部公开仓库](https://github.com/GOOD-123-CPU?tab=repositories)

欢迎通过对应项目的 Issues 交流复现问题、方法讨论和改进建议。

---

### About

My field of study is **Data Science and Big Data Technology**. My projects explore interpretable machine learning, statistical analysis, information retrieval, and data visualization.

Start with **HanBayes** for Chinese sentiment classification and reproducible model comparisons, or **VoxFrontier** for an efficiency and causal-estimation pipeline using synthetic data. **MediRAG** and **ScreenWeaver** extend this work into knowledge applications and visual interfaces.
