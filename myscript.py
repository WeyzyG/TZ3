data = []
with open('data.txt', 'r') as file:
    data = file.readline()
data = list(map(int, data.split()))


def find_max():
    data_max = float('-inf')
    for num in data:
        if num > data_max:
            data_max = num
    return data_max


def find_min():
    data_min = float('+inf')
    for num in data:
        if num < data_min:
            data_min = num
    return data_min


def find_sum():
    global data_sum
    data_sum = 0
    for num in data:
        data_sum += num
    return data_sum


def find_prod():
    data_prod = 1
    for num in data:
        data_prod *= num
    return data_prod


def find_mean():
    data_mean = data_sum / len(data)
    return data_mean


print("Максимальное число в файле:", find_max())
print("Минимальное число в файле:", find_min())
print("Сумма чисел в файле:", find_sum())
print("Произведение чисел в файле:", find_prod())
print("Среднее арифметическое чисел в файле:", find_mean())
