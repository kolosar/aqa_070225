# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

three_lines_alice = """Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to, said the Cat.
I don't much care where, said Alice.
Then it doesn't matter which way you go, said the Cat. so long as I get somewhere,Alice added as an explanation.
Oh, you're sure to do that, said the Cat, if you only walk long enough"""
print("three_lines_alice:",three_lines_alice)
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті \'
escape_characters = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print("Ecranated line:", escape_characters)
# task 03 == Виведіть змінну alice_in_wonderland на дру
print("Alica in wonderland:", escape_characters)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб бул
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_area =  azov_sea + black_sea
print("Total area of Black and Azov sea=", total_area, "km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""


storage1  = 375291 - 222950
storage2  = 250449 - storage1
storage3 = 222950 - storage2
print("storage1 =", storage1, "storage2 =", storage2, "storage3 =", storage3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
number_of_month = 18
fee = 1179
final_cost = number_of_month * fee
print("Computer cost:", final_cost, "uah")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8 
b = 9907 % 9
c = 2789 % 5 
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("8019 : 8 = ", a)
print("9907 : 9 = ", b)
print("2789 : 5 = ", c)
print("7248 : 6 = ", d)
print("7128 : 5 = ", e)
print("19224 : 9 = ", f)




# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
final_sum = (4 * 274) + (2 * 218) + (4 * 35) + 350 + (3 * 21)
print ("Final money amount for birthday party =", final_sum)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pages_amount = 232 / 8
print("Photo pages amount to stick photos:", pages_amount)
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
liters_gasoline = 1600 / 100 * 9
fuel_number = liters_gasoline / 48
print("Liters of gasoline to drive from Kharkiv to Budapest= ", liters_gasoline)
print("Number of fuels to drive from Kharkiv to Budapest= ", fuel_number)