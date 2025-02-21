# tuple
empty_tuple = ()
single_element_tuple = (42,)
multi_tuple = ("a", 34, True)
print("first in tuple:", multi_tuple[0])
print("last in tuple", multi_tuple[-1])

my_tuple = (1, 2, 3, 2, 4, 2, 5, "hi", "hello", "smth", 6, 7, 8, 9, 10)
what_we_look = 2
count_of_2 = my_tuple.count(what_we_look)
print(count_of_2)
index_3 = my_tuple.index("hi")
print("Index 'hi' in my_tuple:", index_3)

subset = my_tuple[2:9:2]
print(subset)

reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

print("Associate multivar")
user_a, user_b, c, d, *other = my_tuple
print(user_a)
print(user_b)
print(c)
print(d)
print(other)

*user_a, user_b, c, d, other = my_tuple
print(user_a)
print(user_b)
print(c)
print(d)
print(other)

user_a, user_b = ("user a", "user b")

# List
my_list = []
my_list_values = ["a", 123, "Heroyam Slava", 1.25]
print(my_list_values[0])
print(my_list_values[2])
print(my_list_values[-1])

print(my_list_values[1:4])
print("id", id(my_list))
my_list.append("FRI")
print("id", id(my_list))
print(my_list)

# my_list.append(["SUN", "ANY"])
my_list.extend(["SUN", "ANY"])
print(my_list)
my_list.insert(-1, "la-la-la")
my_list.insert(2, "???")
print(my_list)
my_list.remove("la-la-la")
print(my_list)
deleted_var = my_list.pop(-2)
print(deleted_var)
print(my_list)

# for i in my_list:
#     print(i)
#     element_index = my_list.index(i)
#     my_list.pop(element_index) # Error can be here

# print(my_list.index("la-la-la"))

print("aaaa" in my_list)
print('SUN' in my_list)
my_string = "kdfjsdlkfjdaklfjdfkldsjfkldasfjadl"
print("aaaa" in my_string)
print("kfjd" in my_string)


my_list.extend(['MON', 'TUE', 'WED', 'THU'])
print("my_list", my_list)

first, middle, last, *four  =  my_list 
print(first)
print(middle)
print(last)
print(four)
my_int_list = [3, 6, 3, 4, 2, 1, 0 ,5, 7, 10.11, 7]
int_sorted = sorted(my_int_list)
var = my_int_list.sort()
print(my_int_list)
print(int_sorted)
print(var)

fruits =  ["яблуко", "апельсин", "банан", "bb", "бб", "груша", "слива",]
print(sorted(fruits))
print(fruits.sort())

my_string = "Привіт, світ!"
list_from_string = list(my_string)
print(list_from_string)

my_range = range(1, 6)
list_from_range = list(my_range)
print(list_from_range)

my_tuple = (10, 20, 30, 40, 50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# list comprehension 
divs = [x / 2 for x in range(1, 21)]
print(divs)

# Set
my_set = {1, 2, 4, 5, 3, 3, 3, 3,}
print(my_set)
print("Is 3 in set?", 3 in my_set)
my_set.add(6)
# """ Виконуєм к-ду додавання в сет, але вона нічого не повертає тобто None """
print(my_set)
my_set.remove(6)
print(my_set)
print(set(my_tuple))
print(set(list_from_tuple))
set_from = set(my_int_list)
print(set_from)
print(my_int_list)
print(len(set_from))
print(len(my_int_list))

my_set.update({13, 7})
print(my_set)
set2 = {3, 4, 5, 6}
set3 = {4, 3, 2, 1}

logical_union = my_set | set2
print(logical_union)

logical_intersection = my_set & set2
print(logical_intersection)


logical_difference = my_set - set2
print("my_set - set2", logical_difference)
logical_difference_2 = set2 - my_set
print("set2 - my_set", logical_difference_2)

logical_symmetric_difference = my_set ^ set2
print(logical_symmetric_difference)

# Dictionary
en_ukr_dict = {"key": "ключ", "hi": "привіт", "love": "любов", "job": "робота", 
               #"learn": "навчатися"
               }
print(en_ukr_dict["key"])
print(en_ukr_dict["love"])
user = {0:"aaaa", 1:"bbbb", (1, 2): "tra-la-la"}
print(user[(1, 2)])
print('key' in en_ukr_dict)
print('ключ' in en_ukr_dict)
print("Iteration for dict")
for k in en_ukr_dict:
    print(k)

for v in en_ukr_dict.values():
    print(v)

for key, value in en_ukr_dict.items():
    print(key, value)

print(en_ukr_dict.get("learn", "Unknow key value"))

ukrainian_letters = set("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" +
                            "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'")
name = "Олександр"

diff =  set(name) - ukrainian_letters
print(True if not diff else False)

yet_other_dict = {"aleph": [1, "a", "b", {"love": "sex"}]}

print(yet_other_dict["aleph"][-1]["love"])
