#14.8.
#До програми з клавіатури надходить послідовність цифр.
#Послідовність задається доти, щоки користувач не введе слово «досить».
#Слід зауважити, що користувач не є дисциплінованим і може заміть цифр вводити будь-що.
#Якщо користувач вводить з клавіатури число більше за 9, то програма ініціює виключення RuntimeError.
#Якщо користувач вводить число менше за 0, то програма ініціює виключення TypeError.
#Якщо користувач вводить дійсне значення з діапазону від 0 до 9, то програма ініціює виключення ValueError.
#Підрахувати кількість виключень кожного типу, що виникають у програмі.

suma_runtime = 0
suma_type = 0
suma_value = 0

while True:
    try:
        n = input("Введіть послідовність цифр, або слово 'досить', щоб закінчити:")
        if n == 'досить':
           break
        number = float(n)
    
        if number > 9:
            raise RuntimeError("Число більше 9")
        elif number < 0:
            raise TypeError("Число менше 0")
        elif 0 <= number <= 9:
            raise ValueError("Дійсне значення від 0 до 9")
    except RuntimeError:
        suma_runtime += 1
    except TypeError:
        suma_type += 1
    except ValueError:
        suma_value += 1
    
print("Кількість виключень RuntimeError: ", suma_runtime)
print("Кількість виключень TypeError: ", suma_type)
print("Кількість виключень ValueError: ", suma_value)