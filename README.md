# David Zhu

**数据科学与大数据技术 · Data Science and Big Data Technology**

你好，我是 David Zhu。我关注**可解释机器学习、统计与因果分析、知识检索和数据可视化**，把分析方法落实为可复现的实验和可运行的应用。

I build reproducible data science projects and AI applications, with a focus on interpretable models, causal analysis, retrieval, and visualization.

[精选项目](#精选项目) · [研究结果](#研究结果) · [更多探索](#更多探索) · [全部仓库](https://github.com/GOOD-123-CPU?tab=repositories)

## 精选项目

| 项目 | 解决的问题 | 从这里开始 |
| :--- | :--- | :--- |
| **[HanBayes](https://github.com/GOOD-123-CPU/hanbayes)** | 中文情感分类：贝叶斯基线、特征加权与可解释预测 | [模型对比结果](https://github.com/GOOD-123-CPU/hanbayes/blob/main/results/final_test_metrics.csv) · [算法说明](https://github.com/GOOD-123-CPU/hanbayes/blob/main/docs/algorithm.md) |
| **[VoxFrontier](https://github.com/GOOD-123-CPU/voxFrontier)** | 直播效率分析：DEA、归因、Double ML 与反事实模拟 | [方法与假设](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/methodology.md) · [复现指南](https://github.com/GOOD-123-CPU/voxFrontier/blob/main/docs/user_guide.md) |
| **[MediRAG](https://github.com/GOOD-123-CPU/medirag-open)** | 医疗文档问答：多路检索、融合、重排序与引用溯源 | [检索链路](https://github.com/GOOD-123-CPU/medirag-open/blob/main/docs/rag-pipeline.md) · [启动与评估边界](https://github.com/GOOD-123-CPU/medirag-open#readme) |
| **[ScreenWeaver](https://github.com/GOOD-123-CPU/screenweaver)** | 配置驱动的数据大屏：Vue 3、TypeScript 与 ECharts | [在线演示](https://good-123-cpu.github.io/screenweaver/) · [完整配置示例](https://github.com/GOOD-123-CPU/screenweaver/blob/main/public/configs/city-ops.json) |
| **[Retail Audit Agent](https://github.com/GOOD-123-CPU/retail-audit-agent)** | 零售审计演示：资料解析、规则识别、AI 解释与报告流程 | [功能与本地体验](https://github.com/GOOD-123-CPU/retail-audit-agent#readme) |
| **[Research Figure Workbench](https://github.com/GOOD-123-CPU/research-figure-workbench)** | 科研制图工作流：数据溯源、图表检查与可编辑导出 | [工作流与使用说明](https://github.com/GOOD-123-CPU/research-figure-workbench#readme) |

## 研究结果

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

## 更多探索

- **知识与 AI 应用**：[LexAtlas 法律知识检索](https://github.com/GOOD-123-CPU/LexAtlas) · [NutriMentor 营养教育](https://github.com/GOOD-123-CPU/nutrimentor) · [OpenInterview 智能面试](https://github.com/GOOD-123-CPU/OpenInterview)
- **金融与业务研究**：[AlphaDebate 多智能体研究](https://github.com/GOOD-123-CPU/AlphaDebate-FinResearch) · [绿证交易平台](https://github.com/GOOD-123-CPU/green-cert-trading) · [绿色金融文献综述](https://github.com/GOOD-123-CPU/green-finance-high-quality-development-review)

## 交流

欢迎通过对应项目的 **Issues** 讨论方法、反馈问题或交流复现结果。项目的安装步骤、依赖和适用边界以各仓库文档为准。
