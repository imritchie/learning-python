# ./data.txt前面的./可以省略
# read() 返回全部文件内容的字符串
f = open("txt/data.txt", encoding="utf-8")  # 默认是r读取模式
print(f.read())
f.close()

# readline() 返回一行内容的字符串
f1 = open("txt/data1.txt", "r", encoding="utf-8")
line = f1.readline()
while line != "":
    print(line)
    line = f1.readline()
f1.close()

# readlines() 返回全部文件内容组成的列表
f2 = open("txt/data2.txt", "r", encoding="utf-8")
lines = f2.readlines()
f2.close()
for line in lines:
    print(line)

with open("txt/data.txt", encoding="utf-8") as f:
    print(f.read())
