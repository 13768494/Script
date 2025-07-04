import os
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *

U = GetLogicalDriveStrings()
U_list = U.split('\x00')
U_list.pop(-1)

for UP in U_list:
    if GetDriveType(UP) == 2:   # 不同盘符类型：https://learn.microsoft.com/zh-cn/windows/win32/api/fileapi/nf-fileapi-getdrivetypea
        break
print(f"检测到目标盘:{UP}")

count = 0
for root,ds,fs in os.walk(UP):  # 该盘符内所有目标文件都可以获取
    for files in fs:
        if ".txt" in files:    # 目标文件类型
            file_path = root + "\\" + files
            save_path = "C:\\Users\\123\Desktop\\1\\新建文件夹\\" + files
            CopyFile(file_path, save_path ,False)
            count += 1
print(f"已复制{count}个文件")
