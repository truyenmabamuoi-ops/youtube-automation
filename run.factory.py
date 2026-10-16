import os
import time
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def main():
    print("🚀 Khởi động hệ thống tự động hóa YouTube thành công!")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Chào buổi tối, hệ thống đã sẵn sàng.")
    print(response.text)

if __name__ == "__main__":
    main()
