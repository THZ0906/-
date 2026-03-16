# 简单 Chatbot 示例（DeepSeek API）

## 项目简介

本项目实现了一个简单的 Chatbot，通过 Python 调用 DeepSeek 模型 API，实现用户输入问题并获得 AI 回复。

功能流程：

用户输入问题 → 调用 DeepSeek API → 输出模型回答

---

## 环境要求

Python >= 3.8

安装依赖：

```
pip install -r requirements.txt
```

---

## API Key 配置

1. 注册 DeepSeek 账号
   https://platform.deepseek.com

2. 创建 API Key

3. 在代码中替换：

```
api_key="YOUR_API_KEY"
```

---

## 运行程序

```
python chatbot.py
```

---

## 示例

```
你: 什么是机器学习
AI: 机器学习是人工智能的一个分支...
```

---

## 项目结构

```
chatbot-demo
│
├── chatbot.py
├── requirements.txt
└── README.md
```

---

## 说明

本项目使用 OpenAI 兼容接口调用 DeepSeek 模型 `deepseek-chat` 实现对话。

