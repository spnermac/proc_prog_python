numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
n = len(numbers)
a = 0
for i in range(n):
    if type(numbers[i]) == int:
        a += numbers[i]
    else:
        j = i
numbers[j] = a/n
print("Измененный список:", numbers)
