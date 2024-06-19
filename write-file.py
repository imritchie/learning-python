# w 覆盖写入，没有文件时会创建新文件，会清空原文件
# a 追加写入，没有文件时会创建新文件，不会清空原文件，而是追加内容
# r+ 同时支持读写，覆盖
# a+ 同时支持读写，追加

with open("txt/write1.txt", "w", encoding="utf-8") as f:
    f.write("朝辞白帝彩云间\n")
    f.write("千里江陵一日还\n")

with open("txt/write1.txt", "a", encoding="utf-8") as f:
    f.write("两岸猿声啼不住\n")

with open("txt/write1.txt", "r+", encoding="utf-8") as f:
    f.write("轻舟已过万重山\n")  # r+，会覆盖掉第一句
    # 此时文件指针在第一行末尾
    print(f.read())

with open("txt/write1.txt", "a+", encoding="utf-8") as f:
    f.write("轻舟已过万重山\n")  # a+ ，不会覆盖掉第一句
    # 此时文件指针在文件末尾
    f.seek(0)  # 将文件指针移动到文件开头
    print(f.read())  # 现在可以打印文件的全部内容
