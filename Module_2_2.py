number1 = int(input("Введите первое число: " ))
print(number1)
number2 = int(input("Введите второе число: "))
print(number2)
number3 = int(input("Введите третье число: "))
print(number3)
if number1 == number2 and number2 == number3 and number1 == number3:
    print(3)
elif number1 == number2 or number1 == number3 or number2 == number3:
    print(2)
elif number1 != number2:
    print(0)



