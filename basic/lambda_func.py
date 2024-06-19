# 求和函数
def sum_num(num1, num2):
    return num1 + num2


# 转换成匿名函数
# 函数名 = lambda 参数 : 返回值
# sum_num = lambda num1, num2: num1 + num2
# (匿名函数)(参数值)
print((lambda num1, num2: num1 + num2)(5, 7))
