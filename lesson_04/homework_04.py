adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print("Replaced end of pharagraph with a space: ", adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("...."," ")
print("Replaced end of .... with a space: ", adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.split()
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer)

print("Removed 2 or more spaces: ", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print("Number of h in the text: ", count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()

count = sum(map(str.istitle, words))

print("Number of capitals in the text = ", count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index = adwentures_of_tom_sawer.find("Tom")
index_2 = adwentures_of_tom_sawer.find("Tom", index+1)
print("Index of second entity of Tom in the text = ", index_2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print("spitted by dot: ", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lower = fourth_sentence.lower()
print("4th sentence to lower case: ", fourth_sentence_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
find = adwentures_of_tom_sawer.find("By the time")
if find != -1: 
    print(f"Found on the position {find}.")
else:
    print(f"Sentence not found.")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[4] # Я знаю, що треба [-1] індекс застосувати, але він чомусь не працює, нічого не виводить. 
new_split = last_sentence.split()
count_words = len(new_split)
print("Numer of words in the last sentence = ", count_words)
