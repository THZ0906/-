from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.deepseek.com"
)

def chat():
    print("=== 简单 Chatbot (DeepSeek) ===")
    print("输入 exit 退出\n")

    while True:
        user_input = input("你: ")

        if user_input.lower() == "exit":
            print("聊天结束")
            break

        # 调用模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个有帮助的AI助手"},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        print("AI:", answer)
        print()


if __name__ == "__main__":
    chat()