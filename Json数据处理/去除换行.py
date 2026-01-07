with open("./data.txt",'r',encoding='utf-8') as f:
    with open("results.txt",'w',encoding='utf-8') as ff:
        for i in f:
            if i != "\n":
                ff.write(i)
    ff.close()
f.close()
