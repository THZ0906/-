
# 🧠 人脸识别 Web 应用（Face Recognition System）

## 📌 项目简介

本项目基于 Python 实现一个简单的人脸识别系统，集成了人脸检测、人脸特征提取（128维编码）以及人脸识别功能，并通过 Web 界面进行可视化展示。

用户可以上传图片，系统会自动检测人脸位置并进行识别（若在人脸库中存在）。

---

## 🚀 技术栈

* Python
* face_recognition（人脸检测与特征提取）
* OpenCV（图像处理）
* Streamlit（Web界面）
* NumPy（数值计算）

---

## 📂 项目结构

```
face_app/
│
├── src/
│   ├── face_utils.py      # 人脸检测与处理
│   └── recognize.py       # 人脸识别逻辑
│
├── data/
│   └── known_faces/       # 已知人脸库
│
├── app.py                 # 主程序（Streamlit界面）
├── requirements.txt       # 依赖文件
└── README.md              # 项目说明
```

---

## ⚙️ 环境配置

### 1️⃣ 创建虚拟环境（推荐）

```bash
python -m venv face_env
```

激活环境：

* Windows：

```bash
face_env\Scripts\activate
```

---

### 2️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install face_recognition opencv-python streamlit numpy
```

---

## ▶️ 运行项目

```bash
streamlit run app.py
```

打开浏览器访问：

```
http://localhost:8501
```

---

## 🧾 使用说明

1. 打开网页界面
2. 上传一张图片
3. 系统自动：

   * 检测人脸位置
   * 提取人脸特征
   * 与人脸库比对
4. 显示识别结果（姓名或 Unknown）

---

## 🧑‍🤝‍🧑 人脸库说明

路径：

```
data/known_faces/
```

要求：

* 每张图片只包含一个人脸
* 文件名即识别名称（如：zhangsan.jpg）
* 支持 jpg / png 格式

示例：

```
zhangsan.jpg
lisi.png
```

---

## 🔍 核心功能

### ✔ 人脸检测

使用 HOG + CNN 方法检测人脸位置

### ✔ 人脸编码

提取每张人脸的 128 维特征向量

### ✔ 人脸识别

通过特征向量比对实现身份识别

### ✔ 可视化展示

通过 Streamlit 展示识别结果和人脸框

---

## ⚠️ 常见问题

### ❌ 无法导入 cv2

👉 原因：numpy 版本不兼容
👉 解决：安装 numpy==1.26.4

---

### ❌ 无法导入 face_recognition

👉 原因：dlib 未正确安装
👉 解决：

```bash
pip install dlib-bin
```

---

### ❌ 识别结果全是 Unknown

👉 原因：

* 人脸库未正确加载
* 图片不清晰或无人脸

---
