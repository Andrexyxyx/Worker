tickets = int(input("Введите желаемое количество билетов "))
summa = [0, 0, 0]
count = [0, 0, 0]
for i in range(1, tickets+1):
    print("Для посетителя #",i)
    age = int((input("Введите возраст ")))
    # Вставить номер покупателя
    if 0 < age < 18:
        count[0] = count[0] + 1
        summa[0] = 0
        print("Вход на конференцию бесплатно")
    elif 18 <= age <= 25:
        count[1] = count[1] + 1
        summa[1] = 990
        print("Cумма к оплате: ", summa[1], "рублей")
    elif age > 25:
        count[2] = count[2] + 1
        summa[2] = 1390
        print("Cумма к оплате: ", summa[2], "рублей")
    else:
        print("Введен некорректный возраст")
if count[0] + count[1] + count[2] <= 3:
    print("---------------------------------------------")
    print("Количество приобретаемых билетов -", count[0] + count[1] + count[2], "шт.")
    print("Общая стоимость билетов составит", summa[0] * count[0] + summa[1] * count[1] + summa[2] * count[2], "рублей")
else:
    print("---------------------------------------------")
    print("Общее количество приобретаемых билетов -", count[0] + count[1] + count[2], "шт.")
    print("Общая стоимость билетов со скидкой составит", (summa[0] * count[0] + summa[1] * count[1] + summa[2] * count[2])*0.9, "рублей")
    print("Сумма скидки составит", (summa[0] * count[0] + summa[1] * count[1] + summa[2] * count[2]) * 0.1, "рублей")

