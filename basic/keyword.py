# -*- coding: utf-8 -*-
'''
Welcome to LearnPython.NET
Author: LearnPython.Net
Editor: CoderChiu
'''

#定义一个字符串，表示名字；
strName = "Ritchie"

#定义一个数字，表示年龄；
nAge = 38

#定义一个数字，表示裤兜里有多少钱；
fMoney = 3.5

#参考初级教程[1]补充信息：函数 Print
print("I am %s, I am %d years old, I have %f Yuan." % (strName, nAge, fMoney))

'''
在Python中，使用 % 符号来格式化字符串时，指定的格式符号（如 %s, %d, %f）用于表示将要插入到字符串中的不同类型的变量。这些符号分别表示：

    %s: 表示字符串类型。当你想要在字符串中插入一个字符串变量时，使用 %s。
    %d: 表示整数类型。用于在字符串中插入一个整数变量。
    %f: 表示浮点数类型。用于在字符串中插入一个浮点数变量。
'''
