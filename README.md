<!-- docker build -t ai-analytics:latest . -->
<!-- docker run -d -p 9000:9000 ai-analytics:latest -->
# AI Analytics API

Dự án API cung cấp các dịch vụ phân tích và xử lý văn bản sử dụng trí tuệ nhân tạo, bao gồm chat, embedding, tóm tắt và tạo tag.

## Tính năng

- **Chat AI**: Trò chuyện với mô hình AI Llama3 thông qua Ollama
- **Text Embedding**: Tạo vector embedding cho văn bản sử dụng Sentence Transformers
- **Text Summarization**: Tóm tắt văn bản thành 3 điểm chính
- **Tag Generation**: Tự động tạo tag từ nội dung văn bản

## Cài đặt nhanh

### 1) Cài Python
- Cài Python từ trang chính thức: [python.org](https://www.python.org/downloads/)
- Kiểm tra sau khi cài: `python --version`

### 2) Cài đặt Ollama
- Tải và cài đặt Ollama từ: [ollama.ai](https://ollama.ai/)
- Cài đặt mô hình Llama3: `ollama pull llama3`
- Khởi động Ollama server: `ollama serve`

### 3) Tạo môi trường ảo (virtual environment)
- Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Chạy ứng dụng
Chạy server ở chế độ reload:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Mở: `http://127.0.0.1:8000`

## API Endpoints

### Chat
- **POST** `/api/chat/`
- Tham số: `question` (string), `context` (optional list[string])
- Trả về: Phản hồi từ AI

### Embedding
- **POST** `/api/embedding/`
- Tham số: `text` (string)
- Trả về: Vector embedding của văn bản

### Summarize
- **POST** `/api/summarize/`
- Tham số: `text` (string)
- Trả về: Tóm tắt văn bản thành 3 điểm

### Tag Generation
- **POST** `/api/tag/`
- Tham số: `text` (string)
- Trả về: Danh sách 5 tag được trích xuất

## Công nghệ sử dụng

- **FastAPI**: Framework web API
- **Ollama**: Inference server cho mô hình AI local
- **Llama3**: Mô hình ngôn ngữ lớn
- **Sentence Transformers**: Tạo embedding văn bản
- **Uvicorn**: ASGI server

## Cấu trúc dự án

```
src/
├── main.py                 # Ứng dụng chính FastAPI
├── https/
│   └── api/               # API endpoints
│       ├── chat.py
│       ├── embedding.py
│       ├── summarize.py
│       └── tag.py
├── services/              # Logic xử lý
│   ├── chat.py
│   ├── embedding.py
│   ├── summarize.py
│   ├── tag.py
│   └── ollama_ai_model.py # Tích hợp Ollama
├── models/                # Định nghĩa dữ liệu
└── request/               # Request models
```
