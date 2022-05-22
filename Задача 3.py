# Подсчитать сумму цифр в вещественном числе.

n = input("Введите вещественное число: ") 
suma = 0 
for digit in n:
    if digit.isdigit():
        suma += int(digit) 
print("Сумма цифр в ведённом числе:", suma)
