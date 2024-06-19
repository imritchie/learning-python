class CuteCat:
    def __init__(self):
        self.like = "吃"

cat1 = CuteCat()
print(cat1.like)


class DogClz:
    def __init__(self, arg_name, arg_color):
        self.name = arg_name
        self.color = arg_color

    def func(self):
        print("dog叫唤的方法执行了")
    def eat(self, food):
        print(f"dog吃{food}")

dog_name = "大黄"
dog_color = "金黄色"
dog1 = DogClz(dog_name, dog_color)
print(dog1)
print(dog1.color, dog1.name)
print(f'狗的名字是{dog1.name},'
      f'狗的颜色是{dog1.color}')

print(f'''狗的名字是{dog1.name},
狗的颜色是{dog1.color}''')

dog1.func()
dog1.eat("骨头")