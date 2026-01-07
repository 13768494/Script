import hashlib

E_password = "c91f32789570b51235074de530ccf53d".lower()

with open("C:/Users/123/Desktop/新建文件夹/常用密码.txt", "r", encoding="utf-8") as f:
    for p in f:
        p = p.strip()
        if not p:
            continue

        md5 = hashlib.md5()
        md5.update(p.encode("utf-8"))
        result = md5.hexdigest()

        if result == E_password:
            print(f"OK！密文：{E_password}  明文：{p}  计算密文：{result}")
            exit()
        else:
            print(f"NO！尝试：{p}  计算密文：{result}")

print("未找到")





