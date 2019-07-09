import os
import stat

from db import get_session
from entity import File

SUPPORTED_FILE_TYPE = ('flac', 'dsf', 'dff')


def get_files(path):
    items = os.listdir(path)
    files = []
    for item in items:
        item = os.path.join(path, item)
        if os.path.isdir(item):
            files = files + get_files(item)
        elif os.path.isfile(item):
            info = get_file_info(item)
            if info:
                files.append(info)

    return files


def get_file_info(file):
    info = os.stat(file)
    extension = file.split('.')[-1]
    if stat.S_ISREG(info.st_mode):
        if extension in SUPPORTED_FILE_TYPE:
            ret = File()
            ret.path = os.path.abspath(file)
            ret.folder = '/'.join(file.split('/')[0: -1])
            ret.name = file.split('/')[-1]
            ret.extension = extension
            ret.size = info.st_size
            ret.created_at = format_time(info.st_ctime)
            ret.modified_at = format_time(info.st_mtime)
            return ret


def format_time(localtime):
    """格式化时间的函数"""
    import time
    return time.strftime("%Y%m%d%H%M%S", time.localtime(localtime))


def get_size(number):
    """格式化文件大小的函数"""
    return round(number/1024/1024, 2)


def save_files(files):
    engine, session = get_session()
    #engine.execute(File.__table__.insert(), files)
    #session.bulk_insert_mappings(File, files)
    for file in files:
        session.add(file)
        session.commit()

    session.close()


def is_empty(path):
    return False


def is_empty_audio(path):
    return False


if __name__ == '__main__':
    root = "/Users/gucciwu/Music"
    result = get_files(root)
    save_files(result)
