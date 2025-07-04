import os
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *
from tqdm import tqdm

U = GetLogicalDriveStrings()
U_list = U.split('\x00')
U_list.pop(-1)

count = 0
for root,ds,fs in os.walk("E:\\"):  # 指定盘符
    for files in tqdm(fs):
        if files.lower().endswith((".docx",".txt",".bmp",".pptx",".rar")):  # 指定文件类型
            file_path = root + "\\" + files
            save_path = "F:\\……\\" + files
            CopyFile(file_path, save_path ,False)
            count += 1
print(f"已复制{count}个文件")
