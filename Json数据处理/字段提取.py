with open("./data.txt",'r',encoding="utf-8") as f:
    lines = f.readlines()
    with open("./results.txt",'w',encoding="utf-8") as ff:
        for i in lines:
            if "mobile" in i:
                print(f"{i}",end="")
                ff.write(i)
    ff.close()
f.close()

print("\n")
print("=============================")
print("=============OK==============")
print("=============================")
