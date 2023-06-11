# twz-backend
twz.tw 網站的 FastAPI 後端

## 安裝

1. 複製 repository (需要先設好 SSH 金鑰):
    ```
    $ git clone git@github.com:LcYxT/twz-backend.git
    ```

2. 切換到 project 目錄
    ```
    $ cd twz-backend
    ```

3. 創建虛擬環境:
    ```
    $ python3 -m venv venv
    ```

4. 安裝需要的 dependencies:
    ```
    $ pip install -r requirements.txt
    ```

## 使用方法

1. 開啟 FastAPI 的開發伺服器:
    ```
    $ uvicorn main:app --reload
    ```

2. 在 http://localhost:8000/docs 可以看到API的文件

## 檔案架構 (以 tree -L 2 twz-backend 產生)

```bash
twz-backend
├── static # Static file folder for requested download from api or mwml-bot
├── models # declaration for types and models
├── services # Implementation of services for download and file, etc.
├── utils #  Utilities functions
├── requirements.txt # Python package requirements
├── config.py # Configuration for API
└── main.py # Main FastAPI app
```