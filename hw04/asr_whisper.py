import whisper

def main():
    model = whisper.load_model("base")  # tiny/base/small/medium/large
    result = model.transcribe("myvideo.mp4", language="zh")

    print("===== Whisper 识别结果 =====")
    print(result["text"])

if __name__ == "__main__":
    main()
