# Chatbot AI for health

## 1. Tính năng

- Nghe, nói bằng tiếng việt được với AI
- Lưu lại lịch sự cuộc trò chuyện và có thể lên được kịch bản cho AI

## 2. Cài đặt

- Cài đặt tất cả các thư viện cần thiết của project bằng lệnh sau:

> pip install -r requirement.txt

- Sau khi cài xong, tạo một file `.env` và ghi như sau: `AI_API_KEY=<YOUR API KEY>`.
- Để có `<YOUR API KEY>`, lên trang [Gemini API Key](https://aistudio.google.com/app/apikey) để tạo một key và sau đó paste vào `<YOUR API KEY>`
- Chạy chương trình bằng terminal

> python main.py

- **Lưu ý:** Để reset lại AI, ta chỉ cần xoá file `data.json`.
- Để chương trình phát được nhạc, cần yêu cầu AI khi đưa tên bài hát phải theo định dạng sau `<Tên bài hát>`
