import os
from urllib.parse import urlparse
import yt_dlp


def download_3rd_party(url: str):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    os.system(f'wget -nc -O static/{filename} {url}')


def download_youtube(url: str):
    ydl = yt_dlp.YoutubeDL({
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'static/%(title)s'
    })
    ydl.download([url])
    # os.system(f'yt-dlp --output "static/%(title)s" {url}')
