# Task 16.9.1 - 16.9.2
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'
#     def get_area(self):
#         return self.width * self.height
# rec_1 = Rectangle(5, 10, 50, 100)
# print(rec_1)
# print("Площадь прямоугольника равна: ", rec_1.get_area())
#
# rec_2 = Rectangle(2, 3, 20, 30)
# print(rec_2)
# print("Площадь прямоугольника равна: ", rec_2.get_area())


# Task 16.9.3 - 16.9.4
class Clients:
    def __init__(self, first_name, last_name, city, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.city = city
    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.city}. Баланс: {self.balance} $'
    def guests_output(self):
        return f'{self.first_name} {self.last_name}. г. {self.city}'

list_client = []
client_1 = Clients("Александр", "Овечкин", "Вашингтон", 5000000)
list_client.append(client_1)
print(client_1)

client_2 = Clients("Кирилл", "Капризов", "Миннесота", 9000000)
list_client.append(client_2)
print(client_2)

client_3 = Clients("Никита", "Кучеров", "Тампа", 9500000)
list_client.append(client_3)
print(client_3)
print("-------------------------------------------------------------")
for guest in list_client:
    print(guest.guests_output())