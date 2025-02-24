small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("Task 1*****")
set_from_small_list = set(small_list)
print("Unique small_list elements: ", set_from_small_list)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("Task 2*******")
total = (sum(small_list)) / (len(small_list))
print("Arithmetic mean: ",total)
# task 3. Перевірте, чи є в списку big_list дублікати
print("task 3**********")
set_big_list = set(big_list)
if len(set_big_list) != len(big_list):
    print("Duplicates are found")
else: ("No duplicates")


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику    add_dict
print("task 4**********")
max_value = max(add_dict)
print("Key with the maxvalue: ",max_value)
# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
print("task 5**********")
new_dictionary = {value: key for key, value in base_dict.items()}
print("New swapped disctionary: ", new_dictionary)
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

#sum_dict = {key: (base_dict.get(key, "") + (" " if key in base_dict and key in add_dict else "") + add_dict.get(key, "")).strip()
#            for key in set(base_dict) | set(add_dict)}
#print("Merged  base_dict та add_dict: ", sum_dict)
# task 7.
print("task 7**********")
line = "Створіть множину всіх символів, які входять у заданий рядок"
print("Set from the line: ", set(line))
# task 8. Обчисліть суму елементів двох множин, які не є спільними
print("task 8**********")
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
log_symetric_difference = set_1.symmetric_difference(set_2)
print("The sum of different elements in set_1 and set_2: ", sum(log_symetric_difference))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("task 9**********")
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
set1_from_list1 = set(list_1)
set2_from_list2 = set(list_2)
final_set = set1_from_list1.symmetric_difference(set2_from_list2)
print("Returned unique set: ", final_set)
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежівset person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
##person_list_dic = dict(person_list)
#for name, age in person_list_dic:

#print(person_list_dic)