with open("./data.txt",'r',encoding="utf-8") as f:
    lines = f.read()
    with open("./results.txt",'w',encoding="utf-8") as ff:
        for i in range(len(lines)):
            if lines[i] == ',':
                print(f"{lines[i]}")
                ff.write('\n')
            elif lines[i] == '}':
                ff.write('\n' + '=============================')
            elif lines[i] != '{':
                print(f"{lines[i]}",end="")
                ff.write(lines[i])
    ff.close()
f.close()

print("\n")
print("=============================")
print("=============OK==============")
print("=============================")

