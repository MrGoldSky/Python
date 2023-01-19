from zipfile import ZipFile
import os


def human_read_format(size):
    if size > 1024 ** 3:
        return str(round(size / 1024 / 1024 / 1024)) + "ГБ"
    elif size >= 1024 ** 2:
        return str(round(size / 1024 / 1024)) + "МБ"
    elif size >= 1024:
        return str(round(size / 1024)) + "КБ"
    elif size < 1024:
        return str(size) + "Б"


with ZipFile('input.zip') as myzip:
    for name in myzip.namelist():
        items = name.rstrip("/").split("/")
        if os.path.isfile(name):
            print("  " * (len(items) - 1) + items[-1], human_read_format(os.path.getsize(os.path.abspath(name))))
        else:
            print("  " * (len(items) - 1) + items[-1])