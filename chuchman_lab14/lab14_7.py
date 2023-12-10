#14.7.
#Дано список чисел. Не використовуючи функцію len визначення кількості елементів у цьому списку та не використовуючи цикл по колекції, визначити:
#a)    кількість елементів у списку;
#b)    суму елементів у списку;
#c)    значення найбільшого відношення (частки) серед елементів.

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list_number = []
#A------------------------------------>
try:
   count = 0
   for el in list_number:
      count += 1

#B------------------------------------>

   suma = 0
   for num in list_number:
      suma += num

#C------------------------------------>
   
   max_el = max(list_number)
   for element in list_number:
      max_share = max(element / max_el for element in list_number)
      second_max_share = max(element / max_el for element in list_number if element / max_el != max_share)
   
   print("Кількість елементів у списку:", count)
   print("Сума елементів списк:у", suma)
   print("Частка:", second_max_share)
except ValueError:
   print(f"Помилка: список пустий")