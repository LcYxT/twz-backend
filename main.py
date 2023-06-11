from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.responses import FileResponse
from services.file_service import get_hash_map, get_static_file_list, get_static_file_list
from models.models import ServerDownloadItem
from services.download_service import download_3rd_party, download_youtube
from config import origins
from utils.common import is_valid_url
from typing import Annotated


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "這裡什麼都沒有喔"}


@app.get("/file/list")
async def get_file_list():
    return get_static_file_list()


@app.get("/download/{hashed_file_name}", response_class=FileResponse)
async def get_file(hashed_file_name: str):
    if os.path.exists(f'static/{hashed_file_name}'):
        return f'static/{hashed_file_name}'

    hash_map = get_hash_map()
    if not hashed_file_name in hash_map:
        raise HTTPException(status_code=404, detail="File not found")
    return f'static/{hash_map[hashed_file_name]}'


@app.post("/server-download")
async def get_server_download(item: ServerDownloadItem):
    if not is_valid_url(item.url):
        raise HTTPException(status_code=404, detail="Invalid URL")
    if 'youtube' in item.url or 'youtu.be' in item.url:
        download_youtube(item.url)
    else:
        download_3rd_party(item.url)

    return get_static_file_list()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile, auth_key: str):
    if not auth_key == 'twz':
        return
    save_directory = os.path.expanduser("~/videos")
    os.makedirs(save_directory, exist_ok=True)

    file_path = os.path.join(save_directory, file.filename)
    
    with open(file_path, "wb") as buffer:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break
            buffer.write(chunk)

    return {"filename": file.filename, "saved_path": file_path}