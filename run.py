import os


def format_time(localtime):
    """格式化时间的函数"""
    import time
    return time.strftime("%Y%m%d%H%M%S", time.localtime(localtime))


def format_byte(number):
    """格式化文件大小的函数"""
    return number/1024/1024


def get_files(path):
    items = os.listdir(path)
    files = []
    for item in items:
        item = os.path.join(path, item)
        if os.path.isdir(item):
            files = files + get_files(item)
        elif os.path.isfile(item):
            files.append(get_file_info(item))

    return files


def get_file_info(file):
    info = os.stat(file)
    return info, os.path.abspath(file), get_file_name(file), get_file_extension(file), format_byte(info.st_size), format_time(info.st_atime), format_time(info.st_mtime)


def get_file_name(file):
    p = file.split('/')
    file_name = p[-1]
    name = file_name.split('.')[0]
    return name


def get_file_extension(file):
    return file.split('.')[-1]


if __name__ == '__main__':
    root = "/Users/gucciwu/Music"
    result = get_files(root)
    print(result)
