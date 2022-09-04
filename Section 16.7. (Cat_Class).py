class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def info(self):
        if self.gender == "мальчик":
            print(f' В базе есть кот по имени {self.name}, ему {self.age} лет')
        elif self.gender == "девочка":
            print(f' В базе есть кошка по имени {self.name}, ей {self.age} лет')
        else:
            print("Введите корректный пол животного (мальчик/девочка)")

cat_1 = Cat("Цезарь", "мальчик", 6)
cat_1.info()

cat_2 = Cat("Люся", "девочка", 5)
cat_2.info()

cat_3 = Cat("Мурзик", "кобель", 8)
cat_3.info()