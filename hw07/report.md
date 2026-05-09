## 1. 实验任务说明
本实验完成胸部 X 光片肺炎二分类任务，分类目标为：
- NORMAL（正常）
- PNEUMONIA（肺炎）

实验要求包括数据预处理、模型构建、训练验证过程记录，并在测试集上输出 Accuracy、Precision、Recall、F1-score 四项指标，同时绘制训练曲线与混淆矩阵。

---

## 2. 数据集统计与分析

本实验使用 Chest X-Ray Images (Pneumonia) 数据集。

数据集结构如下：

- chest_xray/train/NORMAL
- chest_xray/train/PNEUMONIA
- chest_xray/test/NORMAL
- chest_xray/test/PNEUMONIA

### 2.1 数据集样本数量统计

| 数据集 | NORMAL | PNEUMONIA | 总计 |
|-------|--------|-----------|------|
| train（原始） | （填入你统计的数量） | （填入你统计的数量） | （填入总数） |
| test | （填入你统计的数量） | （填入你统计的数量） | （填入总数） |

训练集进一步按 8:2 比例划分：

| 子集 | NORMAL | PNEUMONIA | 总计 |
|------|--------|-----------|------|
| train（训练集 80%） | （自动划分结果） | （自动划分结果） | - |
| val（验证集 20%） | （自动划分结果） | （自动划分结果） | - |

### 2.2 类别分布分析
从统计结果可观察到数据集存在明显类别不平衡现象，PNEUMONIA 类样本数量明显多于 NORMAL 类。
因此仅使用 Accuracy 指标无法全面反映模型性能，本实验额外报告 Precision、Recall 和 F1-score 作为评价指标。

---

## 3. 数据预处理与增强策略

### 3.1 图像预处理
- 图像统一缩放至 224×224
- 归一化：rescale = 1/255

### 3.2 数据增强（训练集）
为缓解过拟合并提升泛化能力，对训练集使用以下数据增强：
- 随机旋转 rotation_range=15
- 随机缩放 zoom_range=0.1
- 水平翻转 horizontal_flip=True
- 剪切变换 shear_range=0.1

### 3.3 训练集/验证集划分
使用 ImageDataGenerator 的 validation_split 参数将 train 数据按 8:2 划分：
- training：80%
- validation：20%

---

## 4. 模型结构设计

本实验采用迁移学习方案，使用 ImageNet 预训练 ResNet50 作为特征提取器。

### 4.1 模型结构
模型主要结构如下：

- 输入：224×224×3
- ResNet50（include_top=False，冻结参数）
- GlobalAveragePooling2D
- Dropout(0.3)
- Dense(128, ReLU)
- Dropout(0.3)
- Dense(1, Sigmoid) 输出二分类概率

### 4.2 迁移学习策略
- ResNet50 backbone 冻结（trainable=False）
- 仅训练顶层分类器部分参数

---

## 5. 超参数设置

| 参数 | 数值 |
|------|------|
| 图像输入尺寸 | 224×224 |
| Batch Size | 32 |
| Epoch | 10 |
| 优化器 | Adam |
| 学习率 | 1e-4 |
| Loss 函数 | Binary Crossentropy |
| 输出层激活函数 | Sigmoid |
| 验证集比例 | 0.2 |

---
<img width="1342" height="856" alt="image" src="https://github.com/user-attachments/assets/a9f2752b-0c6e-454d-b88c-ae4b66c76208" />
<img width="1920" height="1440" alt="accuracy_curve" src="https://github.com/user-attachments/assets/6f48aaa4-85e8-4ec3-b5df-a59ab3b2028a" />
<img width="1800" height="1500" alt="confusion_matrix" src="https://github.com/user-attachments/assets/033b57b4-6864-4031-bf30-27914dea3ade" />
<img width="1920" height="1440" alt="loss_curve" src="https://github.com/user-attachments/assets/be98387a-8a8e-470d-9979-0c521734e950" />



