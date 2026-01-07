import hashlib

with open("./mobiles.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

total = len(words)
print(f"已加载候选明文 {total} 条")

with open("./results.txt", "w", encoding="utf-8") as log, \
     open("./MD5.txt", "r", encoding="utf-8") as ff:

    for E_password in ff:
        E_password = E_password.strip().lower()

        log.write("\n=====================================\n")
        log.write(f"正在破解 MD5：{E_password}\n")

        count = 0
        for p in words:
            count += 1
            result = hashlib.md5(p.encode("utf-8")).hexdigest()

            line = f"[{count}/{total}] 尝试：{p} -> {result}\n"
            log.write(line)
            print(line, end="")

            if result == E_password:
                log.write(">>> 成功命中！\n")
                log.write(f"MD5：{E_password}\n")
                log.write(f"明文：{p}\n")
                print(">>> 成功命中！")
                print(f"明文：{p}")
                exit()

print("全部 MD5 已尝试完毕，未找到匹配。")
