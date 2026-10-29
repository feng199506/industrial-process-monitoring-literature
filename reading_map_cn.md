# 阅读地图

由 `scripts/build_reading_map_en.py` 从 catalog_cn.csv 生成。每类前 10 份：先取筛选时标注的前 10 排名（仅限已核验条目），不足 10 份时按阅读优先级（高 > 中 > 低）与编号补足，补足项的理由取“选入理由”。简介与理由依据摘要或官方页面，未通读全文。

## 阅读路线：从统计基础到过程监控、故障诊断与现代深度方法

编号对应 catalog_cn.csv 与 papers/、books/、university_materials/ 中的文件。阶段内按顺序读；带“可选”的可跳过。

### 阶段 0　统计与线性代数基础（1–2 周）
- 书：14-031 NIST/SEMATECH 工程统计手册（先读第 1、6 章），14-017《Mathematics for Machine Learning》（线性代数、PCA 一章），14-011 ESL 第 3、14 章（PLS、PCA）。
- 课：13-010 MIT 18.650（统计推断与检验），13-017 Stanford EE263（2026，最小二乘、SVD/PCA、高斯条件分布）。
- 目的：掌握假设检验、置信限、协方差与 PCA/SVD——之后所有监控统计量（T²、SPE、控制限）都建立在这里。

### 阶段 1　传统质量控制图与统计过程控制（1 周）
- 课：13-001 MIT 2.830J（SPC、控制图、多变量 SPC），可选 13-002 MIT 2.008（2025 年 SPC 讲次）。
- 书：14-001 Dunn《Process Improvement using Data》控制图与潜变量章节。
- 论文：第 01 类子方向“统计过程控制与控制图（传统质量控制图）”“多变量/函数型/剖面控制图”中的条目。
- 注意区分：控制图监控少数质量特性；多变量统计过程监控（MSPM）监控大量过程变量间的相关结构。

### 阶段 2　多变量统计过程监控与潜变量方法（2 周）
- 综述入门：01-001～01-004（过程工业数据分析、AI 对 SPM 的影响、智能状态监测综述、工业 4.0 FDD 综述）。
- 方法：第 02 类前 10（概率 MSPC、主预测分析、子空间表示、分布式分解），再看 02 类中的慢特征分析（含中文 02-039、02-040）与 CCA/CVA 条目。
- 书：14-020《Data-Driven Fault Detection and Reasoning for Industrial Monitoring》、14-022《Process Monitoring, Fault Diagnosis, and Tolerant Control for Complex Industrial Systems》。

### 阶段 3　过程动态、系统辨识与状态估计（2 周，可与阶段 2 并行）
- 过程背景：13-003 MIT 10.450、13-023 BYU 过程动态与控制在线讲义。
- 辨识：13-005 MIT 6.435、13-006 MIT 2.160、13-021 UCCS ECE5560；书 14-007 Brunton & Kutz、14-021《Regularized System Identification》。
- 状态估计：13-020 UCCS ECE5550、13-018 Stanford EE363（2026），书 14-006 Särkkä《Bayesian Filtering and Smoothing》、14-005 Rawlings MPC（移动视界估计章）。
- 用途：理解动态过程、闭环相关性与观测器残差，为第 06、09 类论文做准备。

### 阶段 4　检测：正常状态建模、早期故障与评测（1–2 周）
- 第 04 类前 10（故障进展指数、早期故障集成网络、物理引导残差、保形异常检测）。
- 评测方法必读：第 11 类 11-002（时间序列异常检测严格评测）、11-016（现有基准缺陷），以及 11 类中关于点调整、时间切分和泄漏的条目。读完再看任何“检测率很高”的结果时，先查是否用了点调整、是否随机切分相邻窗口、是否用故障测试数据设阈值（catalog 有对应字段与全文关键词检出）。
- 理论：13-025 MIT 6.432（检测与估计）。

### 阶段 5　诊断与根因分析（2 周）
- 课程与教材：13-019 Linköping TSFS06 故障诊断课程。
- 论文：第 05 类前 10（因果检测方法比较、滞后传递熵、知识融合故障传播、告警伪因果链抑制）；因果背景见 14-018《What If》。
- 中文：05-062（故障传播路径差异化）、05-063（稳定因果动态贝叶斯网络）。

### 阶段 6　复杂工况：动态、多工况、非平稳与迁移（1–2 周）
- 第 06 类前 10：深度迁移学习综述（06-001）、TE 域适应基准（06-002）、单源域泛化、多尺度时间融合多工况诊断。
- 关注验证方式：跨工况、跨批次或时间外推的验证才可作为泛化证据；catalog“时间切分与验证方式”字段多数需全文核实。

### 阶段 7　质量相关监控、软测量与批次过程（2 周）
- 第 07 类前 10（过程-质量残差概率建模、半监督多单元软测量、SO2 软测量、不确定性校准）。
- 第 08 类前 10（数据同步与自动再校准、标签稀疏质量预测、混合无监督批次监控），配合 14-001 的批次 PCA/PLS 案例。

### 阶段 8　机理融合与数字孪生（1–2 周）
- 第 09 类前 10（过程工业数字孪生学习范式、混合建模在数字孪生中的作用、热工水力过程数字孪生、精馏塔 PINN 数字孪生）。
- 书：14-019《Physics-based Deep Learning》、14-025《Informed Machine Learning》。

### 阶段 9　现代深度方法与工业大模型（2 周）
- 深度监控：第 03 类前 10（图自编码器、Transformer 式 DeepFilter、时空 GNN、KAN 自编码器）。
- 大模型与多模态：第 10 类前 10（IPM-FM 基础模型、FaultExplainer、LLM 与诊断工具互补性、S2S-FDD）。阅读时注意：多数仍在 TE 等仿真基准上评估，真实工业验证与可部署性需要全文核实，本库不作“最优”或“可直接部署”的判断。
- 应用落地：第 12 类按行业挑读（钢铁冶金、矿物加工、电力、污水、制药食品、半导体、造纸水泥），优先选数据来源标为“真实工业”的条目。

## 每类优先阅读的 10 份

### 01 工业过程监控基础与综述

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 01-001 | 2017-09-26 | Data Mining and Analytics in the Process Industry: The Role of Machine Learning | 经典高被引综述，建立过程工业数据驱动监控的整体框架，作为入门首读。 | [2017_Ge_DataMiningAnalyticsProcess_en.pdf](papers/2017_Ge_DataMiningAnalyticsProcess_en.pdf) |
| 2 | 01-002 | 2025-02-23 | A Review of Artificial Intelligence Impacting Statistical Process Monitoring and Future Directions | 回顾 SPC/SPM 百年发展并讨论 AI 带来的变化，衔接传统控制图与数据驱动监控。 | [2025_Chang_ReviewArtificialIntelligenceImpacting_en.pdf](papers/2025_Chang_ReviewArtificialIntelligenceImpacting_en.pdf) |
| 3 | 01-003 | 2024-01-03 | Intelligent Condition Monitoring of Industrial Plants: An Overview of Methodologies and Uncertainty Management Strategies | 以化工装置和 TEP 为主线综述智能监控方法及数据不平衡/无标签等实际难点。 | [2024_Ahang_IntelligentConditionMonitoringIndustrial_en.pdf](papers/2024_Ahang_IntelligentConditionMonitoringIndustrial_en.pdf) |
| 4 | 01-004 | 2024-12-25 | Fault Detection and Diagnosis in Industry 4.0: A Review on Challenges and Opportunities | 系统性文献综述，指出工业实施结果缺口与标准化数据集需求。 | [2024_Leite_FaultDetectionDiagnosisIndustry_en.pdf](papers/2024_Leite_FaultDetectionDiagnosisIndustry_en.pdf) |
| 5 | 01-005 | 2024-01-24 | Machine learning for industrial sensing and control: A survey and practical perspective | 过程工业统计/机器学习在传感与控制中的实践视角综述，有助于理解监控在整个自动化体系中的位置。 | [2024_Lawrence_MachineLearningIndustrialSensing_en.pdf](papers/2024_Lawrence_MachineLearningIndustrialSensing_en.pdf) |
| 6 | 01-006 | 2025-10-29 | Statistical Process Monitoring based on Functional Data Analysis | 函数型数据 SPM 综述，覆盖剖面/函数型控制图子方向。 | [2025_Centofanti_StatisticalProcessMonitoringFunctional_en.pdf](papers/2025_Centofanti_StatisticalProcessMonitoringFunctional_en.pdf) |
| 7 | 01-007 | 2026-01-29 | Mathematical and Algorithmic Advances in Machine Learning for Statistical Process Control: A Systematic Review | PRISMA 系统综述机器学习型 SPC，按数据挑战组织方法族。 | [2026_Qiao_MathematicalAlgorithmicAdvancesMachine_en.pdf](papers/2026_Qiao_MathematicalAlgorithmicAdvancesMachine_en.pdf) |
| 8 | 01-008 | 2024-10-08 | new approach to multivariate statistical process control and its application to wastewater treatment process monitoring | 真实污水厂 MSPC 落地案例，关注与现有趋势图系统集成和操作员可用性。 | [2024_Yamanaka_NewApproachMultivariateStatistical_en.pdf](papers/2024_Yamanaka_NewApproachMultivariateStatistical_en.pdf) |
| 9 | 01-009 | 2024-11-27 | Convolutional kernel-based classification of industrial alarm floods | 报警洪水分类代表作，覆盖报警管理子方向。 | [2024_Manca_ConvolutionalKernelClassificationIndustr_en.pdf](papers/2024_Manca_ConvolutionalKernelClassificationIndustr_en.pdf) |
| 10 | 01-010 | 2025-04-22 | Employing Eye Trackers to Reduce Nuisance Alarms | 从人因角度减少扰动报警的实验研究，补充报警管理的操作员维度。 | [2025_Herdt_EmployingEyeTrackersReduce_en.pdf](papers/2025_Herdt_EmployingEyeTrackersReduce_en.pdf) |

### 02 统计与潜变量方法

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 02-001 | 2026-03-19 | Probabilistic Multivariate Statistical Process Control via Kernel Parameter Uncertainty Propagation | 把核参数不确定性传播到控制限，直接针对核 MSPC 控制限过度自信与报警不稳定问题。 | [2026_Duma_ProbabilisticMultivariateStatisticalProc_en.pdf](papers/2026_Duma_ProbabilisticMultivariateStatisticalProc_en.pdf) |
| 2 | 02-002 | 2026-01 | Principal Predictor Analysis With Application to Dynamic Process Monitoring | Qin 团队新提出的动态潜变量方法，开放获取，是动态潜变量方向的最新代表。 | [2026_Chen_PrincipalPredictorAnalysisApplication_en.pdf](papers/2026_Chen_PrincipalPredictorAnalysisApplication_en.pdf) |
| 3 | 02-003 | 2026-04-19 | System representations in subspaces of finite-sample signals and their application to data-driven fault detection | Ding 团队给出数据驱动故障检测的有限样本子空间理论基础，连接子空间辨识与残差生成。 | [2026_Li_SystemRepresentationsSubspacesFinite_en.pdf](papers/2026_Li_SystemRepresentationsSubspacesFinite_en.pdf) |
| 4 | 02-004 | 2024-09-17 | Fault detection and identification using a novel process decomposition algorithm for distributed process monitoring | 分块 PCA 与贡献图的分布式监控方案，方法清晰、可复现。 | [2024_Villagomez_FaultDetectionIdentificationNovel_en.pdf](papers/2024_Villagomez_FaultDetectionIdentificationNovel_en.pdf) |
| 5 | 02-005 | 2024-03 | Dynamic fault detection and diagnosis for alkaline water electrolyzer with variational Bayesian Sparse principal component analysis | 变分贝叶斯稀疏 PCA 在电解制氢真实场景的应用，兼顾概率与稀疏两个子方向。 | [2024_Zhang_DynamicFaultDetectionDiagnosis_en.pdf](papers/2024_Zhang_DynamicFaultDetectionDiagnosis_en.pdf) |
| 6 | 02-006 | 2025-09-24 | High-Dimensional Statistical Process Control via Manifold Fitting and Learning | 从流形视角重构高维动态过程的 Phase II SPC 统计量。 | [2025_Tas_HighDimensionalStatisticalProcess_en.pdf](papers/2025_Tas_HighDimensionalStatisticalProcess_en.pdf) |
| 7 | 02-007 | 2025-01-20 | Investigating the performance of the Phase II Hotelling T2 chart when monitoring multivariate time series observations | 系统检查 T2 统计量在自相关/互相关数据下的误报问题，是控制限设计的基础问题。 | [2025_Nadi_InvestigatingPerformancePhaseII_en.pdf](papers/2025_Nadi_InvestigatingPerformancePhaseII_en.pdf) |
| 8 | 02-008 | 2026-06-23 | A Novel Dynamic Principal Component Analysis Based on Block Dynamic Mode Decomposition for Chemical Process Fault Detection | 改进动态 PCA 的长时依赖与子系统耦合问题，代表动态潜变量化工应用。 | [2026_Yang_NovelDynamicPrincipalComponent_en.pdf](papers/2026_Yang_NovelDynamicPrincipalComponent_en.pdf) |
| 9 | 02-009 | 2024-09-25 | Double-Layer Distributed and Integrated Fault Detection Strategy for Non-Gaussian Dynamic Industrial Systems | 处理高斯/非高斯并存的大规模分布式监控，覆盖多块建模子方向。 | [2024_Dong_DoubleLayerDistributedIntegrated_en.pdf](papers/2024_Dong_DoubleLayerDistributedIntegrated_en.pdf) |
| 10 | 02-010 | 2025-09-24 | Quality-Ensured In-Situ Process Monitoring with Deep Canonical Correlation Analysis | 深度 CCA 将过程签名与离线质量关联，代表 CCA 的非线性扩展。 | [2025_Song_QualityEnsuredSituProcess_en.pdf](papers/2025_Song_QualityEnsuredSituProcess_en.pdf) |

### 03 机器学习与深度学习监控

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 03-001 | 2026-02-03 | Graph Autoencoder for Process Monitoring | 图结构学习、重构式监控与因果可解释性三者结合，且有真实空分装置验证。 | [2026_Zhang_GraphAutoencoderProcessMonitoring_en.pdf](papers/2026_Zhang_GraphAutoencoderProcessMonitoring_en.pdf) |
| 2 | 03-002 | 2025-01-02 | DeepFilter: A Transformer-style Framework for Accurate and Efficient Process Monitoring | 专为过程监控重新设计 Transformer 时序融合，可作注意力方向的基线对照。 | [2025_Wang_DeepFilter_en.pdf](papers/2025_Wang_DeepFilter_en.pdf) |
| 3 | 03-003 | 2026-07-03 | Spatiotemporal Graph Neural Networks for Fault Detection and Structural Learning in Chemical Processes: Use Case on the Tennessee Eastman Process | 直接检验“GNN 注意力=可解释性”这一常见假设，对阅读其他 GNN 论文有校准作用。 | [2026_KHODJA_SpatiotemporalGraphNeuralNetworks_en.pdf](papers/2026_KHODJA_SpatiotemporalGraphNeuralNetworks_en.pdf) |
| 4 | 03-004 | 2025-08-04 | Exploring Kolmogorov–Arnold Networks for Unsupervised Anomaly Detection in Industrial Processes | 以训练数据量为变量的对照实验，回答了自编码器监控对数据量的敏感性。 | [2025_LunaVillagomez_ExploringKolmogorovArnoldNetworksUnsuper_en.pdf](papers/2025_LunaVillagomez_ExploringKolmogorovArnoldNetworksUnsuper_en.pdf) |
| 5 | 03-005 | 2024-10-10 | MOLA: Enhancing Industrial Process Monitoring Using a Multi-Block Orthogonal Long Short-Term Memory Autoencoder | 把深度表示与非参数统计监控量、块融合结合，接近工程化监控框架。 | [2024_Ma_MOLA_en.pdf](papers/2024_Ma_MOLA_en.pdf) |
| 6 | 03-006 | 2024-01-08 | Generative adversarial wavelet neural operator: Application to fault detection and isolation of multivariate time series data | 生成模型监控中少见同时含基准与真实污水厂数据的工作。 | [2024_Rani_GenerativeAdversarialWaveletNeural_en.pdf](papers/2024_Rani_GenerativeAdversarialWaveletNeural_en.pdf) |
| 7 | 03-007 | 2025 | Embedding-Enhanced Graph Attention Networks for Imbalanced Industrial Fault Diagnosis | GNN 诊断中用真实工业数据而非仅 TEP 的代表。 | [2025_Zhang_EmbeddingEnhancedGraphAttention_en.pdf](papers/2025_Zhang_EmbeddingEnhancedGraphAttention_en.pdf) |
| 8 | 03-008 | 2025-02-03 | SensorDBSCAN: Semi-Supervised Active Learning Powered Method for Anomaly Detection and Diagnosis | 对比学习+主动学习的低标注方案，使用多版本 TEP 且公开代码，便于复现。 | [2025_Ivanov_SensorDBSCAN_en.pdf](papers/2025_Ivanov_SensorDBSCAN_en.pdf) |
| 9 | 03-009 | 2026-06-18 | A Multiscale Spatial-Temporal Graph Neural Network With Causal-Augmented Constraints for Industrial Fault Detection | GNN 构图同时利用过程先验知识与因果发现，并在两个真实数据集上验证，弥补多数 GNN 工作只用 TEP 的不足。 | [2026_Lyu_MultiscaleSpatialTemporalGraph_en.pdf](papers/2026_Lyu_MultiscaleSpatialTemporalGraph_en.pdf) |
| 10 | 03-010 | 2024-03-20 | Adversarial Attacks and Defenses in Fault Detection and Diagnosis: A Comprehensive Benchmark on the Tennessee Eastman Process | 系统评测深度诊断模型的对抗脆弱性与防御，是部署深度监控模型前需要了解的鲁棒性问题。 | [2024_Pozdnyakov_AdversarialAttacksDefensesFault_en.pdf](papers/2024_Pozdnyakov_AdversarialAttacksDefensesFault_en.pdf) |

### 04 异常检测与早期故障检测

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 04-001 | 2026-10-12 | Fault Progression Index: A State-Space Monitoring Framework for Early Fault Warning in Industrial Processes | 同时关注检测延迟、退化进展与误报定义，评测协议表述明确。 | [2026_Jitkhamhaeng_FaultProgressionIndex_en.pdf](papers/2026_Jitkhamhaeng_FaultProgressionIndex_en.pdf) |
| 2 | 04-002 | 2024-04-22 | Autoencoder-assisted Feature Ensemble Net for Incipient Faults | 直接攻击 TEP 最难检测的微小故障，是早期故障检测的标志性问题。 | [2024_Gao_AutoencoderAssistedFeatureEnsemble_en.pdf](papers/2024_Gao_AutoencoderAssistedFeatureEnsemble_en.pdf) |
| 3 | 04-003 | 2026-04-15 | Early-warning industrial fault detection based on physics-guided residual learning and calibrated CRNNs | 把阈值设计、概率校准与统计置信区间纳入检测流程，契合本类“控制限设计”核心问题。 | [2026_Khan_EarlyWarningIndustrialFault_en.pdf](papers/2026_Khan_EarlyWarningIndustrialFault_en.pdf) |
| 4 | 04-004 | 2025-02-27 | Conformal Anomaly Detection for Predictive Maintenance in Thermal Power Plants | 以保形推断给出有统计保证的误报控制，是阈值设计的新思路。 | [2025_Kundacina_ConformalAnomalyDetectionPredictive_en.pdf](papers/2025_Kundacina_ConformalAnomalyDetectionPredictive_en.pdf) |
| 5 | 04-005 | 2026-01-18 | Machine Learning-Based Framework for Real Time Detection and Early Prediction of Control Valve Stiction in Industrial Control Systems | 真实工业数据上的“提前量”型预警结果，问题定义贴近现场。 | [2026_Promsricha_MachineLearningFrameworkReal_en.pdf](papers/2026_Promsricha_MachineLearningFrameworkReal_en.pdf) |
| 6 | 04-007 | 2024-09-05 | A method to benchmark high-dimensional process drift detection | 少有的专门针对过程漂移检测的可控基准，补足本类“渐变/漂移”子方向。 | [2024_Wolf_MethodBenchmarkHighDimensional_en.pdf](papers/2024_Wolf_MethodBenchmarkHighDimensional_en.pdf) |
| 7 | 04-008 | 2025-08-08 | Segmented Confidence Sequences and Multi-Scale Adaptive Confidence Segments for Anomaly Detection in Nonstationary Time Series | 自适应阈值并保留误报率保证，直接回应非平稳工况下控制限失效的问题。 | [2025_Li_SegmentedConfidenceSequencesMulti_en.pdf](papers/2025_Li_SegmentedConfidenceSequencesMulti_en.pdf) |
| 8 | 04-009 | 2026-07-17 | Knowledge-Assisted Multi-Graph Dependency Learning for Multivariate Time Series Anomaly Detection in Multi-Stage Industrial Processes | 将过程结构知识引入正常状态依赖建模，体现过程监控与通用时序异常检测的区别。 | [2026_Lee_KnowledgeAssistedMultiGraph_en.pdf](papers/2026_Lee_KnowledgeAssistedMultiGraph_en.pdf) |
| 9 | 04-010 | 2024-07-21 | An Optimal Spatio-Temporal Hybrid Model Based on Wavelet Transform for Early Fault Detection | 针对被噪声淹没的缓慢早期故障，结合小波去噪、时空混合统计量与 KDE 控制限，是“微小故障+控制限”的典型组合。 | [2024_Xing_OptimalSpatioTemporalHybrid_en.pdf](papers/2024_Xing_OptimalSpatioTemporalHybrid_en.pdf) |
| 10 | 04-013 | 2025-05-31 | Automated Anomaly Detection in Blast Furnace Shaft Static Pressure Using Adversarial Autoencoders and Mode Decomposition | （补足）VMD 分解与改进对抗自编码器对高炉炉身静压做无监督异常检测，覆盖偏置、形态变化与突变等多尺度异常。 | [2025_Sun_AutomatedAnomalyDetectionBlast_en.pdf](papers/2025_Sun_AutomatedAnomalyDetectionBlast_en.pdf) |

### 05 故障诊断与根因分析

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 05-001 | 2024-07-29 | A Comparative Study of Causality Detection Methods in Root Cause Diagnosis: From Industrial Processes to Brain Networks | 跨方法统一评测因果根因诊断，适合先建立因果诊断方法的整体认识与评价口径。 | [2024_Zhou_ComparativeStudyCausalityDetection_en.pdf](papers/2024_Zhou_ComparativeStudyCausalityDetection_en.pdf) |
| 2 | 05-002 | 2025-06-26 | Lag-Specific Transfer Entropy for Root Cause Diagnosis and Delay Estimation in Industrial Sensor Networks | 覆盖仿真、实验装置与真实高炉数据的因果根因与时延估计，是因果诊断从基准走向现场的代表。 | [2025_Chen_LagSpecificTransferEntropy_en.pdf](papers/2025_Chen_LagSpecificTransferEntropy_en.pdf) |
| 3 | 05-003 | 2025-04-07 | An EPS-kNN Fault Propagation Analysis Method for Industrial Processes Based on the Fusion of Knowledge and Data | 知识与数据融合的传播路径分析，兼顾 TEP 与合成氨过程，代表知识约束因果诊断路线。 | [2025_Lixin_EPSKNNFaultPropagation_en.pdf](papers/2025_Lixin_EPSKNNFaultPropagation_en.pdf) |
| 4 | 05-004 | 2026-10-16 | Suppressing Spurious Causal Chains in Alarm-Triggered Alarm Phenomena via Liang–Kleeman Information Flow–Max-Min Hill-Climbing Graphs | 报警根因与因果图去伪的新近工作，直接对应报警泛滥场景。 | [2026_Li_SuppressingSpuriousCausalChains_en.pdf](papers/2026_Li_SuppressingSpuriousCausalChains_en.pdf) |
| 5 | 05-005 | 2024-06-19 | Root-KGD: A Novel Framework for Root Cause Diagnosis Based on Knowledge Graph and Industrial Data | 知识图谱与数据联合根因诊断的代表框架。 | [2024_Chen_RootKGD_en.pdf](papers/2024_Chen_RootKGD_en.pdf) |
| 6 | 05-006 | 2024-07-12 | Robustness of Explainable Artificial Intelligence in Industrial Process Modelling | 为诊断可解释性提供“解释是否正确”的评测视角，读其他 XAI 论文前先读。 | [2024_Kantz_RobustnessExplainableArtificialIntellige_en.pdf](papers/2024_Kantz_RobustnessExplainableArtificialIntellige_en.pdf) |
| 7 | 05-008 | 2025-11-17 | Uncovering Causal Drivers of Energy Efficiency for Industrial Process in Foundry via Time-Series Causal Inference | 真实铸造生产数据上“先分工况再做 PCMCI+ 因果发现”的完整流程，可直接借鉴到流程工业根因分析。 | [2025_Ma_UncoveringCausalDriversEnergy_en.pdf](papers/2025_Ma_UncoveringCausalDriversEnergy_en.pdf) |
| 8 | 05-009 | 2024-06-08 | Interpretability of Causal Discovery in Tracking Deterioration in a Highly Dynamic Process | 真实粘胶纤维产线上用含专家知识的因果发现跟踪退化，展示因果图的可解释监控价值。 | [2024_Choudhary_InterpretabilityCausalDiscoveryTracking_en.pdf](papers/2024_Choudhary_InterpretabilityCausalDiscoveryTracking_en.pdf) |
| 9 | 05-011 | 2025-02-19 | Fault Root Cause Analysis Based on Liang–Kleeman Information Flow and Graphical Lasso | （补足）以 Liang–Kleeman 信息流结合图 Lasso 做根因分析，并与传递熵在 TEP 全部故障上对比。 | [2025_Liu_FaultRootCauseAnalysis_en.pdf](papers/2025_Liu_FaultRootCauseAnalysis_en.pdf) |
| 10 | 05-012 | 2026-06-22 | Design of a smart alarming system using transfer entropy-based causality graphs | （补足）以传递熵因果图结合 MEEMD 降噪与时延估计，识别扰动源以缓解报警泛滥。 | [2026_Pisiecki_DesignSmartAlarmingSystem_en.pdf](papers/2026_Pisiecki_DesignSmartAlarmingSystem_en.pdf) |

### 06 动态、多工况与非平稳过程

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 06-001 | 2024-01-02 | A Comprehensive Survey of Deep Transfer Learning for Anomaly Detection in Industrial Time Series: Methods, Applications, and Directions | 迁移/域适应主题的综述入口，先建立方法分类再读具体论文。 | [2024_Yan_ComprehensiveSurveyDeepTransfer_en.pdf](papers/2024_Yan_ComprehensiveSurveyDeepTransfer_en.pdf) |
| 2 | 06-002 | 2024-09-09 | Benchmarking Domain Adaptation for Chemical Processes on the Tennessee Eastman Process | 多工况/域适应研究的公共评测起点，后续多篇跨域诊断工作基于类似设置。 | [2024_Montesuma_BenchmarkingDomainAdaptationChemical_en.pdf](papers/2024_Montesuma_BenchmarkingDomainAdaptationChemical_en.pdf) |
| 3 | 06-004 | 2025-05 | Dual adversarial and contrastive network for single-source domain generalization in fault diagnosis | 单源域泛化到未见工况，贴近过程工业故障样本稀缺的实际。 | [2025_Li_DualAdversarialContrastiveNetwork_en.pdf](papers/2025_Li_DualAdversarialContrastiveNetwork_en.pdf) |
| 4 | 06-005 | 2025-09 | Attention-based multiscale temporal fusion network for uncertain-mode fault diagnosis in multimode processes | 多工况故障诊断中“工况未知”设置的代表。 | [2025_Li_AttentionMultiscaleTemporalFusion_en.pdf](papers/2025_Li_AttentionMultiscaleTemporalFusion_en.pdf) |
| 5 | 06-006 | 2025-08-16 | Few-shot Class-incremental Fault Diagnosis by Preserving Class-Agnostic Knowledge with Dual-Granularity Representations | 少样本类增量诊断，覆盖基准与真实数据，代表持续学习在过程诊断中的新进展。 | [2025_Yang_FewShotClassIncremental_en.pdf](papers/2025_Yang_FewShotClassIncremental_en.pdf) |
| 6 | 06-007 | 2026-04-10 | Drift-Aware Online Dynamic Learning for Nonstationary Multivariate Time Series: Application to Sintering Quality Prediction | 真实冶金过程中“漂移+标签延迟”的在线适应，代表过程漂移方向的现实问题设定。 | [2026_Zhao_DriftAwareOnlineDynamic_en.pdf](papers/2026_Zhao_DriftAwareOnlineDynamic_en.pdf) |
| 7 | 06-008 | 2024-09-22 | Online Multi-Source Domain Adaptation Through Gaussian Mixtures and Dataset Dictionary Learning | 在线多源域适应且在 TEP 上验证，体现“目标工况数据以流形式到达”的现实设定。 | [2024_Montesuma_OnlineMultiSourceDomain_en.pdf](papers/2024_Montesuma_OnlineMultiSourceDomain_en.pdf) |
| 8 | 06-010 | 2026-09-17 | Machine learning-based classification of operating regimes in an urban wastewater treatment plant: a benchmark on reconstructed reference labels | 基于公开真实污水厂数据的运行工况识别评测，标签重建过程透明，便于复现。 | [2026_OviedoBayas_MachineLearningClassificationOperating_en.pdf](papers/2026_OviedoBayas_MachineLearningClassificationOperating_en.pdf) |
| 9 | 06-011 | 2026-06-30 | Fault Diagnosis Under Unknown Operating Conditions Based on Adaptive Graph Learning and Dual-Weighted Contrastive Mechanism | （补足）多源域泛化中同时考虑标签偏移，以自适应图学习和双加权对比机制诊断未知工况故障。 | [2026_Hou_FaultDiagnosisUnknownOperating_en.pdf](papers/2026_Hou_FaultDiagnosisUnknownOperating_en.pdf) |
| 10 | 06-012 | 2024-03-18 | Learning to better see the unseen: Broad-Deep Mixed Anti-Forgetting Framework for Incremental Zero-Shot Fault Diagnosis | （补足）提出增量零样本故障诊断范式，兼顾新故障类别/属性学习与防遗忘。 | [2024_Zhao_LearningBetterSeeUnseen_en.pdf](papers/2024_Zhao_LearningBetterSeeUnseen_en.pdf) |

### 07 质量相关监控与软测量

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 07-001 | 2026-07-03 | Probabilistic Residual Modeling for Sensor-Based Process–Quality Fault Detection in Industrial Systems | 直接对应“质量相关故障检测”核心问题，给出 FDR/FAR 与多基线对比，便于理解该子方向评测方式 | [2026_Zhang_ProbabilisticResidualModelingSensor_en.pdf](papers/2026_Zhang_ProbabilisticResidualModelingSensor_en.pdf) |
| 2 | 07-002 | 2024-07-18 | A deep latent variable model for semi-supervised multi-unit soft sensing in industrial processes | 半监督与多单元软测量的代表作，使用大规模真实工业数据，且讨论向新单元迁移 | [2024_Grimstad_DeepLatentVariableModel_en.pdf](papers/2024_Grimstad_DeepLatentVariableModel_en.pdf) |
| 3 | 07-003 | 2026-09-29 | GRAG-Net: A Gated Residual Autoregressive–Exogenous GRU Soft Sensor for Dynamic SO2 Estimation in Sulfur Recovery Units | 评测设计（时间顺序、未来测试期、强基线如持久性）对本库评测规范有参考价值 | [2026_Alghamdi_GRAGNet_en.pdf](papers/2026_Alghamdi_GRAGNet_en.pdf) |
| 4 | 07-004 | 2026-04-02 | Toward Intrinsically Calibrated Uncertainty Quantification in Industrial Data-Driven Models via Diffusion Sampler | 不确定性量化是软测量可信使用的关键，且含真实合成氨案例 | [2026_Ma_IntrinsicallyCalibratedUncertaintyQuanti_en.pdf](papers/2026_Ma_IntrinsicallyCalibratedUncertaintyQuanti_en.pdf) |
| 5 | 07-005 | 2024 | A Unifying View of Multivariate State Space Models for Soft Sensors in Industrial Processes | 对比型研究，覆盖三个真实过程，有助于理解动态软测量模型选择 | [2024_Liu_UnifyingViewMultivariateState_en.pdf](papers/2024_Liu_UnifyingViewMultivariateState_en.pdf) |
| 6 | 07-006 | 2026-05-30 | Graph Attention-Based Virtual Metrology for Film Deposition Processes in Semiconductor Manufacturing | 虚拟量测子方向代表作，真实生产数据 + 可解释结构 | [2026_Han_GraphAttentionVirtualMetrology_en.pdf](papers/2026_Han_GraphAttentionVirtualMetrology_en.pdf) |
| 7 | 07-007 | 2026-10-26 | Uncertainty-aware virtual metrology for chemical concentration prediction in electroless plating | 同时覆盖稀疏/异步标签与不确定性量化，真实工厂数据 | [2026_Huang_UncertaintyAwareVirtualMetrology_en.pdf](papers/2026_Huang_UncertaintyAwareVirtualMetrology_en.pdf) |
| 8 | 07-009 | 2024-05-16 | Adaptive Temporal–Spatial Pyramid Variational Autoencoder Model for Multirate Dynamic Chemical Process Soft Sensing Application | 多速率软测量子方向近期代表，含工业案例 | [2024_Shen_AdaptiveTemporalSpatialPyramidVariationa_en.pdf](papers/2024_Shen_AdaptiveTemporalSpatialPyramidVariationa_en.pdf) |
| 9 | 07-010 | 2025-09-25 | Soft Measurement Modeling Method Based on Quality-Related Mixed Variational Autoencoder Regression | （补足）把过程变量映射到质量相关/无关两个子空间的混合 VAE 回归，代表质量相关潜变量提取用于多模态软测量 | [2025_Xu_SoftMeasurementModelingMethod_en.pdf](papers/2025_Xu_SoftMeasurementModelingMethod_en.pdf) |
| 10 | 07-011 | 2026-03-12 | Slack More, Predict Better: Proximal Relaxation for Probabilistic Latent Variable Model-Based Soft Sensors | （补足）从变分推断近似误差角度改进非线性概率潜变量软测量模型（Wasserstein 近端松弛），代表概率潜变量软测量理论进展 | [2026_Zou_SlackMorePredictBetter_en.pdf](papers/2026_Zou_SlackMorePredictBetter_en.pdf) |

### 08 批次过程监控

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 08-002 | 2024-06-24 | Data synchronization techniques and their impact on the prediction performance of automated recalibrated soft sensors in bioprocesses | 把批次对齐与软测量重校准联系起来，对实际生物制药批次数据处理有直接参考价值 | [2024_Siegl_DataSynchronizationTechniquesTheir_en.pdf](papers/2024_Siegl_DataSynchronizationTechniquesTheir_en.pdf) |
| 2 | 08-003 | 2024-03-24 | Collaborative Multiple Players to Address Label Sparsity in Quality Prediction of Batch Processes | 同时体现批次二维动态与稀疏质量标签，两个本类关键问题 | [2024_Zhao_CollaborativeMultiplePlayersAddress_en.pdf](papers/2024_Zhao_CollaborativeMultiplePlayersAddress_en.pdf) |
| 3 | 08-004 | 2024-03-19 | Hybrid Unsupervised Learning Strategy for Monitoring Industrial Batch Processes | 少见的直接以“工业批次过程监控”为题的近期 arXiv 工作 | [2024_Frey_HybridUnsupervisedLearningStrategy_en.pdf](papers/2024_Frey_HybridUnsupervisedLearningStrategy_en.pdf) |
| 4 | 08-005 | 2026-05-18 | UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction | 批次过程中阶段识别与异常检测结合的代表，且使用公开实验数据集便于复现 | [2026_Pessoa_UTOPYA_en.pdf](papers/2026_Pessoa_UTOPYA_en.pdf) |
| 5 | 08-006 | 2025-12-03 | Learning From Limited Data and Feedback for Cell Culture Process Monitoring: A Comparative Study | 基准比较类研究，可作为生物制药批次软测量的方法选择参考 | [2025_Peng_LearningLimitedDataFeedback_en.pdf](papers/2025_Peng_LearningLimitedDataFeedback_en.pdf) |
| 6 | 08-007 | 2026-06-17 | Oxygen-based soft-sensing of glucose demand in Chinese hamster ovary fed-batch cultures across scales | 面向工业生物制药实际操作的软测量，跨规模验证 | [2026_Jossen_OxygenSoftSensingGlucose_en.pdf](papers/2026_Jossen_OxygenSoftSensingGlucose_en.pdf) |
| 7 | 08-009 | 2025-02 | Quality-related and Quality-irrelevant Fault Detection and Diagnosis in Batch Fermentation Process Based on NSSAE | 批次场景下的质量相关故障检测，连接 07 与 08 两类问题 | [2025_LIU_QualityRelatedQualityIrrelevant_en.pdf](papers/2025_LIU_QualityRelatedQualityIrrelevant_en.pdf) |
| 8 | 08-010 | 2025-11-10 | Artificial intelligence and machine learning‐assisted digital applications for biopharmaceutical manufacturing | 生物制药批次生产的近期综述，可作为 08 类生物过程部分的入口 | [2025_Panjwani_ArtificialIntelligenceMachineLearningass_en.pdf](papers/2025_Panjwani_ArtificialIntelligenceMachineLearningass_en.pdf) |
| 9 | 08-011 | 2026-09-08 | Data-Driven Approach for Bioreactor Monitoring and Prediction in Monoclonal Antibody Production | （补足）针对工业单抗补料分批数据高维、不规则采样、大量缺失的完整数据驱动流程：插补、模型基准、可解释性与软测量 | [2026_Kubra_DataDrivenApproachBioreactor_en.pdf](papers/2026_Kubra_DataDrivenApproachBioreactor_en.pdf) |
| 10 | 08-012 | 2024-09-03 | Uncertainty Quantification Using Ensemble Learning and Monte Carlo Sampling for Performance Prediction and Monitoring in Cell Culture Processes | （补足）小样本下用集成学习与蒙特卡洛采样量化细胞培养性能预测与拉曼葡萄糖监测的不确定性 | [2024_Khuat_UncertaintyQuantificationEnsembleLearnin_en.pdf](papers/2024_Khuat_UncertaintyQuantificationEnsembleLearnin_en.pdf) |

### 09 机理融合、数字孪生与过程建模

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 09-001 | 2024-07-02 | Learning Paradigms and Modelling Methodologies for Digital Twins in Process Industry | 过程工业数字孪生建模方法的综述入口。 | [2024_Mayr_LearningParadigmsModellingMethodologies_en.pdf](papers/2024_Mayr_LearningParadigmsModellingMethodologies_en.pdf) |
| 2 | 09-003 | 2024-12-02 | Navigating industry 4.0 and 5.0: the role of hybrid modelling in (bio)chemical engineering’s digital transition | 工业视角的混合建模综述，补充数字孪生/PIML 两篇综述的过程工程背景。 | [2024_Gargalo_NavigatingIndustry40_en.pdf](papers/2024_Gargalo_NavigatingIndustry40_en.pdf) |
| 3 | 09-004 | 2026-02-25 | Data-Driven Supervision of a Thermal-Hydraulic Process Towards a Physics-Based Digital Twin | 数字孪生直接服务过程 FDD 的案例。 | [2026_Imhogiemhe_DataDrivenSupervisionThermal_en.pdf](papers/2026_Imhogiemhe_DataDrivenSupervisionThermal_en.pdf) |
| 4 | 09-005 | 2026-03-25 | Physics-Informed Neural Network Digital Twin for Dynamic Tray-Wise Modeling of Distillation Columns under Transient Operating Conditions | 物理约束嵌入化工单元动态模型的典型做法，可作为监控用机理-数据模型的模板。 | [2026_Patra_PhysicsInformedNeuralNetwork_en.pdf](papers/2026_Patra_PhysicsInformedNeuralNetwork_en.pdf) |
| 5 | 09-007 | 2024-08-07 | Self‐tuning moving horizon estimation of nonlinear systems via physics‐informed machine learning Koopman modeling | 机理-数据融合用于状态估计的代表，状态估计是软测量与诊断的基础。 | [2024_Yan_SelftuningMovingHorizonEstimation_en.pdf](papers/2024_Yan_SelftuningMovingHorizonEstimation_en.pdf) |
| 6 | 09-008 | 2026-06-21 | Observability- and Identifiability-Guided Sensor-Set Design for Digital-Twin-Assisted Consolidated Bioprocessing | 把可观性/可辨识性分析用于监测传感器设计，是“模型支持监控”的直接例子。 | [2026_Yeboah_ObservabilityIdentifiabilityGuidedSensor_en.pdf](papers/2026_Yeboah_ObservabilityIdentifiabilityGuidedSensor_en.pdf) |
| 7 | 09-009 | 2025-02-15 | Machine learning enhanced grey box soft sensor for melt viscosity prediction in polymer extrusion processes | 典型串联式灰箱软测量（机理+残差学习），结构清晰，可作为混合建模入门例子。 | [2025_Perera_MachineLearningEnhancedGrey_en.pdf](papers/2025_Perera_MachineLearningEnhancedGrey_en.pdf) |
| 8 | 09-010 | 2025-06-23 | Dynamic hybrid modeling: Incremental identification and model predictive control | 动态混合模型辨识方法，可迁移到监控用混合模型的构建。 | [2025_Caspari_DynamicHybridModeling_en.pdf](papers/2025_Caspari_DynamicHybridModeling_en.pdf) |
| 9 | 09-011 | 2025-10-07 | Scale-up of complex molecular reaction system by hybrid mechanistic modeling and deep transfer learning | （补足）分子级动力学机理模型与性质约束的深度迁移学习结合，跨实验室-中试尺度预测石脑油催化裂化产物分布。 | [2025_Chen_ScaleUpComplexMolecular_en.pdf](papers/2025_Chen_ScaleUpComplexMolecular_en.pdf) |
| 10 | 09-012 | 2026-02-15 | Learning-based data-enabled moving horizon estimation with application to membrane-based biological wastewater treatment process | （补足）无显式模型时以 Koopman LPV 代理与 Willems 基本引理构建凸的数据驱动 MHE，应用于膜生物反应器污水处理。 | [2026_Li_LearningDataEnabledMoving_en.pdf](papers/2026_Li_LearningDataEnabledMoving_en.pdf) |

### 10 工业大模型与多模态监控

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 10-001 | 2026-09-08 | IPM-FM: A Foundation Model with Consensus Feature Selection for Industrial Process Monitoring | 少有的明确以“工业过程监控基础模型”为目标且在真实炼油装置长期数据上评估的工作。 | [2026_Cao_IPMFM_en.pdf](papers/2026_Cao_IPMFM_en.pdf) |
| 2 | 10-002 | 2024-12-19 | FaultExplainer: Leveraging Large Language Models for Interpretable Fault Detection and Diagnosis | 化工过程 LLM 辅助诊断的代表性开源式工作，同时报告了局限，便于把握能力边界。 | [2024_Khan_FaultExplainer_en.pdf](papers/2024_Khan_FaultExplainer_en.pdf) |
| 3 | 10-003 | 2026-10-04 | When LLMs Sit Above Diagnostic Tools: Unrealized Complementarity in Industrial Fault Diagnosis | 提供 LLM 诊断“整合不一定增益”的定量证据，可校准对 LLM 辅助诊断的预期。 | [2026_Kim_WhenLLMsSitAbove_en.pdf](papers/2026_Kim_WhenLLMsSitAbove_en.pdf) |
| 4 | 10-004 | 2026-03-09 | S2S-FDD: Bridging Industrial Time Series and Natural Language for Explainable Zero-shot Fault Diagnosis | 直接处理 LLM 与工业时序之间的语义鸿沟，且面向过程工业数据。 | [2026_Li_S2SFDD_en.pdf](papers/2026_Li_S2SFDD_en.pdf) |
| 5 | 10-005 | 2024-06-13 | Cross-Modal Learning for Anomaly Detection in Complex Industrial Process: Methodology and Benchmark | 少见的真实工业“图像+过程变量”跨模态监控基准，可复现性潜力高。 | [2024_Wu_CrossModalLearningAnomaly_en.pdf](papers/2024_Wu_CrossModalLearningAnomaly_en.pdf) |
| 6 | 10-006 | 2025-07-09 | Early Warning of Abnormal Operating Modes via Feature Extraction from Cross-Section Frame at Discharge End for Sintering Process | 过程工业中“图像+过程变量”融合预警的真实现场案例。 | [2025_Hao_EarlyWarningAbnormalOperating_en.pdf](papers/2025_Hao_EarlyWarningAbnormalOperating_en.pdf) |
| 7 | 10-007 | 2026-06-10 | Large Language Models in Process Systems Engineering: Opportunities, Architectures, and Industrial Deployment Challenges | 覆盖 PSE 全链条且专门评述故障检测与诊断，适合作为本类阅读框架。 | [2026_Gopaluni_LargeLanguageModelsProcess_en.pdf](papers/2026_Gopaluni_LargeLanguageModelsProcess_en.pdf) |
| 8 | 10-008 | 2026-08-20 | Large reasoning models for abnormal situation management in safety-critical industrial processes | 在全厂级基准上给出通用推理模型运行时处置异常工况的定量结果，并含程序化校验接口，代表 LLM 进入过程运行闭环的前沿。 | [2026_Alhazmi_LargeReasoningModelsAbnormal_en.pdf](papers/2026_Alhazmi_LargeReasoningModelsAbnormal_en.pdf) |
| 9 | 10-009 | 2026-06-22 | Safe integration of Large Language Models into industrial process control: a multi-agent architecture with P&amp;ID-grounded validation | 系统讨论 LLM 安全接入过程控制的架构与 P&ID 验证，并给出从零幻觉到高违规率的性能边界。 | [2026_Schall_SafeIntegrationLargeLanguage_en.pdf](papers/2026_Schall_SafeIntegrationLargeLanguage_en.pdf) |
| 10 | 10-010 | 2025-03-04 | RAAD-LLM: Adaptive Anomaly Detection Using LLMs and RAG Integration | 在塑料制造厂真实数据上验证 LLM+RAG 无微调异常检测，是 LLM 直接处理过程时序检测的代表案例。 | [2025_RussellGilbert_RAADLLM_en.pdf](papers/2025_RussellGilbert_RAADLLM_en.pdf) |

### 11 数据集、基准与评测方法

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 11-001 | 2025-06-25 | 3W Dataset 2.0.0: a realistic and public dataset with rare undesirable real events in oil wells | 真实油井事件、专家标注且持续版本化的公开过程工业数据集，适合作为真实数据评测的首选参照。 | [2025_Vargas_3WDataset200_en.pdf](papers/2025_Vargas_3WDataset200_en.pdf) |
| 2 | 11-002 | 2021-09-11 | Towards a Rigorous Evaluation of Time-series Anomaly Detection | 点调整（PA）评测偏差的源头文献，阅读本类其余评测方法文献前应先读。 | [2021_Kim_RigorousEvaluationTimeSeries_en.pdf](papers/2021_Kim_RigorousEvaluationTimeSeries_en.pdf) |
| 3 | 11-003 | 2026-10-01 | Time series data with and without anomalies from a continuous distillation plant | 实测连续精馏装置异常数据，可与 TE 仿真结论直接对照。 | [2026_Muraleedharan_TimeSeriesDataWithout_en.pdf](papers/2026_Muraleedharan_TimeSeriesDataWithout_en.pdf) |
| 4 | 11-004 | 2026-04-10 | Automated batch distillation process simulation for a large hybrid dataset for deep anomaly detection | 实验与仿真配对的批次精馏异常数据，可研究仿真-实测差距。 | [2026_Werner_AutomatedBatchDistillationProcess_en.pdf](papers/2026_Werner_AutomatedBatchDistillationProcess_en.pdf) |
| 5 | 11-006 | 2025-06-13 | Temporal cross-validation impacts multivariate time series subsequence anomaly detection evaluation | 直接检验时间切分方式对评测结论的影响，关系到泄漏与过度乐观。 | [2025_Hespeler_TemporalCrossValidationImpacts_en.pdf](papers/2025_Hespeler_TemporalCrossValidationImpacts_en.pdf) |
| 6 | 11-007 | 2026-07-12 | Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection | 检验 PA 替代指标在择优报告下是否可被刷高，给出报告规范依据。 | [2026_Lyu_DidWeActuallyFix_en.pdf](papers/2026_Lyu_DidWeActuallyFix_en.pdf) |
| 7 | 11-008 | 2025-11-14 | Enabling predictive maintenance in district heating substations: A labelled dataset and fault detection evaluation framework based on service data | 服务记录验证标签的真实运行数据，并给出准确性/可靠性/提前量评测框架。 | [2025_Roelofs_EnablingPredictiveMaintenanceDistrict_en.pdf](papers/2025_Roelofs_EnablingPredictiveMaintenanceDistrict_en.pdf) |
| 8 | 11-011 | 2025-12 | A multimodal dataset for process monitoring and anomaly detection in industrial CNC milling | （补足）工业 CNC 铣削的多模态过程监控与异常检测数据集，记录控制器信号。 | [2025_Strobel_MultimodalDatasetProcessMonitoring_en.pdf](papers/2025_Strobel_MultimodalDatasetProcessMonitoring_en.pdf) |
| 9 | 11-014 | 2026-08-08 | In a Streaming World, Should You Stand Still- A Comprehensive Benchmark of Anomaly Detection in Streams | （补足）KDD 2026 大规模流式与静态时序异常检测统一评测基准。 | [2026_Parrino_StreamingWorldShouldYou_en.pdf](papers/2026_Parrino_StreamingWorldShouldYou_en.pdf) |
| 10 | 11-015 | 2026-03-19 | Revisiting OmniAnomaly for Anomaly Detection: performance metrics and comparison with PCA-based models | （补足）在统一阈值与评测协议下重新比较 OmniAnomaly 与 PCA 类模型，检验深度模型增益。 | [2026_Alves_RevisitingOmniAnomalyAnomalyDetection_en.pdf](papers/2026_Alves_RevisitingOmniAnomalyAnomalyDetection_en.pdf) |

### 12 工业应用

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 12-001 | 2024-06-06 | A Survey of Data-Driven Soft Sensing in Ironmaking System: Research Status and Opportunities | 钢铁冶金行业软测量的近期综述，可快速建立该行业问题全貌 | [2024_Yan_SurveyDataDrivenSoft_en.pdf](papers/2024_Yan_SurveyDataDrivenSoft_en.pdf) |
| 2 | 12-002 | 2026-09-01 | Multimodal Flotation Sensing: A Systematic Review of State Identification and Sensor Readiness | 矿物加工行业的近期系统综述，覆盖软测量走向工业部署的工程要求 | [2026_Akishev_MultimodalFlotationSensing_en.pdf](papers/2026_Akishev_MultimodalFlotationSensing_en.pdf) |
| 3 | 12-003 | 2026-08-14 | A Physics-Informed Multi-Task Soft Sensor for Uncertainty-Aware Slag Tin Content Prediction in Top-Blown Tin Smelting | 真实有色冶炼数据、稀疏标签与时间顺序评估兼具 | [2026_Ma_PhysicsInformedMultiTask_en.pdf](papers/2026_Ma_PhysicsInformedMultiTask_en.pdf) |
| 4 | 12-004 | 2024-06-07 | Data-Driven Modeling of the Spray Drying Process. Process Monitoring and Prediction of the Particle Size in Pharmaceutical Production | 制药真实生产数据、关键质量属性在线监控的范例 | [2024_Lopez_DataDrivenModelingSpray_en.pdf](papers/2024_Lopez_DataDrivenModelingSpray_en.pdf) |
| 5 | 12-005 | 2026-04-14 | Physics-Guided Multi-Task Learning for Small-Sample Soft Sensing: Simultaneous Prediction of Kappa Number and Viscosity in Continuous Kraft Pulping | 造纸行业稀缺的近期过程软测量文献 | [2026_Zhang_PhysicsGuidedMultiTask_en.pdf](papers/2026_Zhang_PhysicsGuidedMultiTask_en.pdf) |
| 6 | 12-007 | 2026-10-12 | Fault Diagnosis in a Wastewater Treatment Plant Based on Linguistic Ordered Weighted Averaging and Deep Learning Pooling | 污水处理全流程故障诊断代表，覆盖传感器、执行器与单元故障 | [2026_BeneytoRodriguez_FaultDiagnosisWastewaterTreatment_en.pdf](papers/2026_BeneytoRodriguez_FaultDiagnosisWastewaterTreatment_en.pdf) |
| 7 | 12-008 | 2025-08-09 | Data-Driven Fouling Detection in Refinery Preheat Train Heat Exchangers Using Neural Networks and Gradient Boosting | 炼厂换热网络结垢监测，石化行业中少见的近期可路由应用 | [2025_Andrijic_DataDrivenFoulingDetection_en.pdf](papers/2025_Andrijic_DataDrivenFoulingDetection_en.pdf) |
| 8 | 12-009 | 2025-08-25 | Flame monitoring and anomaly detection in steel reheating furnaces based on thermal video using a hybrid AI computer vision system | 钢厂真实数据、带操作员看板的落地型监测系统 | [2025_Vanhaeverbeke_FlameMonitoringAnomalyDetection_en.pdf](papers/2025_Vanhaeverbeke_FlameMonitoringAnomalyDetection_en.pdf) |
| 9 | 12-010 | 2026-01-30 | Data-Driven Soft Sensing for Raw Milk Ethanol Stability Prediction | 乳品行业三年真实生产数据的质量软测量 | [2026_Shen_DataDrivenSoftSensing_en.pdf](papers/2026_Shen_DataDrivenSoftSensing_en.pdf) |
| 10 | 12-011 | 2025-11-18 | Resolving Steam Turbine Casing Thermal Management Challenges with a Dual Attentive Bi-GRU Soft Sensor for Transient Operation | （补足）370 MW 燃煤机组中压缸缸体温度的双注意力 Bi-GRU 软测量，覆盖启停与变负荷瞬态 | [2025_KrukGotzman_ResolvingSteamTurbineCasing_en.pdf](papers/2025_KrukGotzman_ResolvingSteamTurbineCasing_en.pdf) |

### 13 著名大学课程教材与讲义

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 13-001 | Spring 2008 | 2.830J/6.780J/ESD.63J Control of Manufacturing Processes (SMA 6303) | SPC 与多变量 SPC 的系统课程，直接对应传统控制图与 MSPM 入门 | [MIT_2830J_2008Spring_OCWCoursePackage_en.zip](university_materials/MIT_2830J_2008Spring_OCWCoursePackage_en.zip) |
| 2 | 13-019 | VT 2024（2024 春季，课程仓库 2024-10 最后更新） | TSFS06 Diagnosis and Supervision | 专门的故障检测与诊断课程，覆盖残差、隔离与统计检验 | [Linkoping_TSFS06_2024VT_LectureSlides_en](university_materials/Linkoping_TSFS06_2024VT_LectureSlides_en) |
| 3 | 13-003 | Spring 2006 | 10.450 Process Dynamics, Operations, and Control | 化工过程动态与控制基础，理解被监控对象 | [MIT_10450_2006Spring_OCWCoursePackage_en.zip](university_materials/MIT_10450_2006Spring_OCWCoursePackage_en.zip) |
| 4 | 13-023 | 在线课程网站（学期见课程表页） | Process Dynamics and Control (BYU ChE course site) | 化工过程动态与控制在线讲义（含辨识与 MPC），可边读边做 | [BYU_ProcessDynamicsControl_Online_HTML_en.zip](university_materials/BYU_ProcessDynamicsControl_Online_HTML_en.zip) |
| 5 | 13-005 | Spring 2005 | 6.435 System Identification | 系统辨识完整课程，动态建模与机理融合的基础 | [MIT_6435_2005Spring_OCWCoursePackage_en.zip](university_materials/MIT_6435_2005Spring_OCWCoursePackage_en.zip) |
| 6 | 13-006 | Spring 2006 | 2.160 Identification, Estimation, and Learning | 辨识、估计与学习合一，衔接状态估计与数据驱动建模 | [MIT_2160_2006Spring_OCWCoursePackage_en.zip](university_materials/MIT_2160_2006Spring_OCWCoursePackage_en.zip) |
| 7 | 13-020 | 课程页未注明学期（讲义版权年见各讲首页） | ECE5550 Applied Kalman Filtering | 卡尔曼滤波及其非线性扩展的工程讲义，用于状态估计监控 | [UCCS_ECE5550_AppliedKalmanFiltering_LectureNotes_en](university_materials/UCCS_ECE5550_AppliedKalmanFiltering_LectureNotes_en) |
| 8 | 13-025 | Spring 2004 | 6.432 Stochastic Processes, Detection, and Estimation | 检测与估计理论，故障检测阈值与假设检验的理论来源 | [MIT_6432_2004Spring_OCWCoursePackage_en.zip](university_materials/MIT_6432_2004Spring_OCWCoursePackage_en.zip) |
| 9 | 13-017 | Summer 2026 | EE263 Introduction to Linear Dynamical Systems | 2026 年线性动态系统讲义，含 SVD/PCA 与 MMSE 估计 | [Stanford_EE263_2026Summer_LectureSlides_en](university_materials/Stanford_EE263_2026Summer_LectureSlides_en) |
| 10 | 13-002 | Spring 2025 | 2.008 Design and Manufacturing II | 2025 年制造课程，含过程变异与 SPC 的最新讲次 | [MIT_2008_2025Spring_OCWCoursePackage_en.zip](university_materials/MIT_2008_2025Spring_OCWCoursePackage_en.zip) |

### 14 教科书、专著与参考书

| # | 编号 | 首次公开/版本 | 标题 | 理由 | 文件 |
|---|---|---|---|---|---|
| 1 | 14-001 | 2023-02-01 版（Zenodo 10d109；作者另有 2026.10.06 HTML 版） | Process Improvement using Data | 从控制图到 PCA/PLS 与批次监控的开放教材，最适合作为第一本书 | [Dunn_ProcessImprovementUsingData_2023ed_en.pdf](books/Dunn_ProcessImprovementUsingData_2023ed_en.pdf) |
| 2 | 14-020 | 2022 Springer 开放获取版 | Data-Driven Fault Detection and Reasoning for Industrial Monitoring | 开放获取的工业监控专著，覆盖检测、分类、隔离与推理 | [Wang_DataDrivenFaultDetectionReasoning_2022_en.pdf](books/Wang_DataDrivenFaultDetectionReasoning_2022_en.pdf) |
| 3 | 14-022 | 2025 Springer 开放获取版（Steven X. Ding 纪念文集） | Process Monitoring, Fault Diagnosis, and Tolerant Control for Complex Industrial Systems | 2025 年过程监控与故障诊断文集，反映近年研究前沿（质量相关、多工况等） | [Luo_ProcessMonitoringFaultDiagnosisTolerantControl_2025_en.pdf](books/Luo_ProcessMonitoringFaultDiagnosisTolerantControl_2025_en.pdf) |
| 4 | 14-031 | 官网章节 PDF 全集（8 章；首版 2003，持续维护） | NIST/SEMATECH e-Handbook of Statistical Methods | NIST 官方手册第 6 章是控制图与 SPC 的权威参考 | [NIST_SEMATECH_eHandbookStatisticalMethods_en](books/NIST_SEMATECH_eHandbookStatisticalMethods_en) |
| 5 | 14-006 | 第 2 版（2023，作者官网在线版） | Bayesian Filtering and Smoothing (2nd ed.) | 状态估计（卡尔曼/粒子滤波）系统教材，机理融合监控必备 | [Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf](books/Sarkka_BayesianFilteringSmoothing_2ndEd_en.pdf) |
| 6 | 14-011 | 第 2 版第 12 次印刷 | The Elements of Statistical Learning (2nd ed.) | PCA、PLS、核方法等统计学习方法的标准参考 | [Hastie_ElementsOfStatisticalLearning_2ndEd_en.pdf](books/Hastie_ElementsOfStatisticalLearning_2ndEd_en.pdf) |
| 7 | 14-007 | 作者官网 PDF（版本见扉页） | Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control | SVD、DMD、SINDy 等数据驱动动力学建模，衔接系统辨识 | [Brunton_DataDrivenScienceEngineering_en.pdf](books/Brunton_DataDrivenScienceEngineering_en.pdf) |
| 8 | 14-005 | 第 2 版（作者官网 PDF，第 5 次印刷） | Model Predictive Control: Theory, Computation, and Design (2nd ed.) | 含移动视界估计专章的化工过程状态估计权威参考 | [Rawlings_ModelPredictiveControl_2ndEd_en.pdf](books/Rawlings_ModelPredictiveControl_2ndEd_en.pdf) |
| 9 | 14-016 | 2023 版 | Probabilistic Machine Learning: Advanced Topics | 状态空间、变化点/异常检测与因果推断章节，支撑现代方法 | [Murphy_ProbabilisticMachineLearningAdvanced_2023_en.pdf](books/Murphy_ProbabilisticMachineLearningAdvanced_2023_en.pdf) |
| 10 | 14-018 | 2026 年作者官网版 | Causal Inference: What If | 因果推断标准入门，为因果诊断与根因分析打基础 | [Hernan_CausalInferenceWhatIf_2026_en.pdf](books/Hernan_CausalInferenceWhatIf_2026_en.pdf) |

