import random

array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
any_number = int(input("Введите число, которое находится в диапазоне чисел введенной ранее последовательности: "))

# Функция сортировки вводимой последовательности
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
    left_nums = [n for n in array if n < q]

    center_nums = [q] * array.count(q)
    right_nums = [n for n in array if n > q]
    return quick_sort(left_nums) + center_nums + quick_sort(right_nums)

sort_array = quick_sort(array)
print(f'''Упорядоченный по возрастанию список: {sort_array}
***************************************************************''')

# Функция двоичного поиска в отсортированной последовательности
def binary_search(array, any_number, left, right):
    try:
        if left > right:
            return('''В списке нет введенного элемента. Ищем ближайшие элементы
----------------------------------------------------------''')
        middle = (right + left) // 2
        if array[middle] == any_number:
            return middle
        elif any_number < array[middle]:
            return binary_search(array, any_number, left, middle - 1)
        else:
            return binary_search(array, any_number, middle + 1, right)
    except IndexError:
        return 'ВВЕДЕННОЕ ЧИСЛО БОЛЬШЕ ВСЕХ ЧИСЕЛ В ВВЕДЕННОЙ РАНЕЕ ПОСЛЕДОВАТЕЛЬНОСТИ. ВВЕДИТЕ КОРРЕКТНОЕ ЧИСЛО'

# if binary_search(sort_array, any_number, 0, len(sort_array)) == '''В списке нет введенного элемента. Ищем ближайшие элементы
# ----------------------------------------------------------''':
#     min_elem = min(sort_array, key=lambda x: (abs(x - any_number), x)) #Минимальный элемент в отсортированном списке
#     indx = sort_array.index(min_elem) #Индекс минимального элемента в отсортированном списке
#     max_index = indx + 1
#     min_index = indx - 1
#     if min_elem < any_number:
#         print(f'''В списке нет введенного элемента
# Ближайший элемент, который меньше введенного: {min_elem}, Его номер индекса - №{indx}
# Ближайший элемент, который больше введенного: {sort_array[max_index]}, Его номер индекса - №{max_index}''')
#     elif min_index < 0:
#         print("ВВЕДЕННОЕ ЧИСЛО МЕНЬШЕ ВСЕХ ЧИСЕЛ В ВВЕДЕННОЙ РАНЕЕ ПОСЛЕДОВАТЕЛЬНОСТИ. ВВЕДИТЕ КОРРЕКТНОЕ ЧИСЛО")
#     elif min_elem > any_number:
#         print(f'''В списке нет введенного элемента
# Ближайший элемент, который больше введенного: {min_elem}, Его номер индекса - №{sort_array.index(min_elem)}
# Ближайший элемент, который меньше введенного: {sort_array[min_index]}, Его номер индекса - №{min_index}''')
#     elif sort_array.index(min_elem) == 0:
#         print(f'Индекс введенного элемента: {sort_array.index(min_elem)}')
# else:
#     min_elem = min(sort_array, key=lambda x: (abs(x - any_number), x))  # Минимальный элемент в отсортированном списке
#     print(f'''В списке есть точное значение элемента. Индекс ближайшего введенного элемента: №{binary_search(sort_array, any_number, 0, len(sort_array))}'
#     Номер индекса ближайщего элемента, который меньше введенного - №{binary_search(sort_array, any_number, 0, len(sort_array)) - 1}
#     Номер индекса ближайщего элемента, который больше или равен введенному - №{binary_search(sort_array, any_number, 0, len(sort_array)) + 1}''')