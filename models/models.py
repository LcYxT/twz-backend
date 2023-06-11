from pydantic import BaseModel, HttpUrl
from typing import TypedDict


class StaticFile(TypedDict):
    name: str
    size: str
    link: str
    modified_time: str


class ServerDownloadItem(BaseModel):
    url: HttpUrl
