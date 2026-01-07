with open("./data.txt",'r',encoding="utf-8") as f:
    arr = set()

    for line in f:
        if "password" in line:
            arr.add(line.strip())

    with open("./results.txt", "w", encoding="utf-8") as ff:
        for line in arr:
            print(line)
            ff.write(line + "\n")
    ff.close()
f.close()

print("\n")
print("=============================")
print("=============OK==============")
print("=============================")
