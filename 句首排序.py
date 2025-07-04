# 考试时可方便查找题目答案
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
f.close()

line = []
for i in range(len(text)):
    line.append(text[i].strip())

line = list(set(line))
line = sorted(line)

with open("result.txt", "w", encoding="utf-8") as f:
    for i in range(len(line)):
        f.write(line[i] + "\n")
f.close()
