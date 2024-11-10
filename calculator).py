num1 = float(input("Перше число: "))
operator = input("Дія (+, -, *, /): ")
num2 = float(input("Друге число: "))

if operator == '+':
    print("Результат:", num1 + num2)
elif operator == '-':
    print("Результат:", num1 - num2)
elif operator == '*':
    print("Результат:", num1 * num2)
elif operator == '/':
    print("Результат:", num1 / num2)
