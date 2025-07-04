# 可使用pyinstaller -F -i 打包
import os
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *
from tqdm import tqdm

U = GetLogicalDriveStrings()
U_list = U.split('\x00')
U_list.pop(-1)

path = ".\\save\\"
if not os.path.exists(path):
    os.makedirs(path)

count = 0
for root,ds,fs in os.walk("E:\\"):
    for files in tqdm(fs):
        if files.lower().endswith((".docx",".bmp",".pptx",".rar",".txt")):
            file_path = root + "\\" + files
            save_path = path + files
            CopyFile(file_path, save_path ,False)
            count += 1
            print(file_path)
print(f"已复制{count}个文件")
