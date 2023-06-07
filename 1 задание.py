# Старинная игра: У кого цифр больше
var1 = int(input("Введите первую переменную: "))
var2 = int(input("Введите вторую переменную: "))

digits = {}
digits[var1] = len(str(var1))
digits[var2] = len(str(var2))

if digits[var1] > digits[var2]:
    print("В первой переменной больше цифр")
elif digits[var1] < digits[var2]:
    print("Во второй переменной больше цифр")
else:
    print("Количество цифр в обеих переменных равно")
