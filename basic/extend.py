class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "在吃东西")


class DogClz(Animal):
    def __init__(self, arg_color, name, age):
        super().__init__(name, age)
        self.color = arg_color

    def dog_func(self):
        print(self.name + "叫唤的方法执行了")


class CatClz(Animal):
    def __init__(self, arg_color, name, age):
        super().__init__(name, age)
        self.color = arg_color

    def cat_func(self):
        print(self.name + "的方法执行了")


dog1 = DogClz("小黄", "球球", 3)
dog1.eat()

cat1 = CatClz("银", "树", 1)
cat1.cat_func()
