import hashlib
import os
from datetime import datetime
from typing import List
from models.models import StaticFile


def get_size(file_path):
    file_size = os.path.getsize(file_path)
    exponents_map = {'Bytes': 0, 'KB': 1, 'MB': 2, 'GB': 3}
    unit = 'Bytes'
    for u in exponents_map.keys():
        if ((file_size / 1024 ** exponents_map[u]) < 1000):
            unit = u
            break
    size = file_size / 1024 ** exponents_map[unit]
    return f'{round(size, 1)}{unit}'


def get_hashed_file_name(file_name: str):
    hash_object = hashlib.sha256(file_name.encode())
    hash_value = hash_object.hexdigest()
    return hash_value


def get_static_file_list() -> List[StaticFile]:
    files = os.listdir('./static')
    files = list(filter(lambda f: '.mp4' in f, files))
    file_list = list(map(lambda f: {
        'name': f,
        'size': get_size(f'./static/{f}'),
        'link': f'/api/download/{get_hashed_file_name(f)}',
        'modified_time': datetime.fromtimestamp(os.path.getctime(f'./static/{f}')).strftime('%Y-%m-%d %H:%M:%S')
    }, files))
    return file_list


def get_hash_map():
    hash_map = {}
    file_list = get_static_file_list()
    for f in file_list:
        hashed = get_hashed_file_name(f['name'])
        hash_map[hashed] = f['name']
    return hash_map
