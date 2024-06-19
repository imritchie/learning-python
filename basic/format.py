# 第一种写法 format(args) {参数的下标}
name = "张三"
age = 19

message_content = """
    你好呀，
怎么回事。
    {0}表示第一个参数，
    {1}是第二个参数。
""".format(name, age)
print(message_content)

# 第二种写法 format(args) {参数名}
hobbyVal = "唱跳rap"
dialogVal = "谈论天气"

dialog_content = """
    爱好是{hobby}，
    当前会话{dialog}。
""".format(dialog=dialogVal, hobby=hobbyVal)
print(dialog_content)

# 第三种 '''前面+f
year = "蛇"
month = "Jan"

date_content = f'''
    今年是{year}年,
    现在是{month}月。
'''
print(date_content)
