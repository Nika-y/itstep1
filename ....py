result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {
    10: 2,
    2: 5,
    "123": 4,
    18: 0,
    8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Ділення на нуль (a={key}, b={value})")
    except ValueError as e:
        print(f"Помилка: {e} (a={key}, b={value})")
    except IndexError as e:
        print(f"Помилка: {e} (a={key}, b={value})")
    except TypeError as e:
        print(f"Помилка: Неправильний тип даних (a={key}, b={value}) - {e}")

print("Результат:", result)
