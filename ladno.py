import os
import getpass
from datetime import datetime

BASE_DIR = "C:\\"


def file_collector(path: str):  # Переходит в указанную директорию и получает информацию о ней
    got_path = os.path.join(BASE_DIR, path)
    result = {'dirs': [], 'files': []}
    print(f"[{datetime.now():{'%Y-%m-%d %H:%M:%S'}}] Перехожу в {got_path}...")
    for path, dirnames, filenames in os.walk(got_path):
        for dir_ in dirnames:
            result['dirs'].append(dir_)
        for file in filenames:
            result['files'].append(file)
    return result


def record(data: dict):  # Записывает результат в текстовый файл
    with open(file='logs.txt', mode='w') as file:
        file.write('\n{:-^50}\n'.format('Directories'))
        for dir_ in data['dirs']:
            file.write(f'\t{dir_}\n')
        file.write('\n{:-^50}\n'.format('Files'))
        for files in data['files']:
            file.write(f'\t{files}\n')
    print(f"[{datetime.now():{'%Y-%m-%d %H:%M:%S'}}] Успешно сохранено в {file.name}")


userPath = '\\'.join(input(f"{getpass.getuser()}, введите путь к директории через пробел: ").split())
gotFiles = file_collector(userPath)
record(gotFiles)
