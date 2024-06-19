try:
    user_input = float(input("输入数字："))
except ValueError:
    print("输入了不合理数字")
except ZeroDivisionError:
    print("除零错误")
except:  # 如果上面的错误捕捉到了，后面的错误类型就不会再捕捉
    print("发生了未知错误")
else:
    print("没有错误时运行")
finally:
    print("无论是否发生错误都会运行")
