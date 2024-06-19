# round(number, ndigits=None)
# 返回 number 舍入到小数点后 ndigits 位精度的值。
# ndigits 可为任意整数值（正数、零或负数），返回值与 number 的类型相同。
x = round(1.0835, 3)
print(x)
print(round(13.0845, 2))
print(round(23.0855, 2))
print(round(23.0845, 3))
print(round(23.0855, 3))


print("-----------")
# 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。
x1 = round(0.6)
print(x1)

# 对于支持 round() 方法的内置类型，结果值会舍入至最接近的 10 的负 ndigits 次幂的倍数；如果与两个倍数同样接近，则选用偶数。
# 因此，round(0.5) 和 round(-0.5) 均得出 0 而 round(1.5) 则为 2。
x2 = round(0.5)  # >>> 0
x3 = round(-0.5)  # >>> 0
x4 = round(1.5)  # >>> 2
print(x2)
print(x3)
print(x4)


# 由于大多数十进制小数实际上都不能以浮点数精确地表示。 对浮点数执行 round() 的行为可能会令人惊讶。
x5 = round(2.675, 2)  # >>> 2.67，并不是2.68
print(x5)
