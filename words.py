from random import choice, randint

# создание списка слов для игры из текстового файла
words = [] # пустой список под слова
# файл со словами
file = open("russian_nouns.txt")
# добавляем в множество из файла слова длинее 5 букв
for line in file:
    if len(line) > 6:
        words.append(line[:-1])
file.close()

#word = choice(words).upper() # загадываем слово из списка

# нужно написать функцию которая маскирует
# все буквы в слове кроме двух:
def get_word():
    word = choice(words).upper()
    visible_letter_1 = randint(0, len(word) - 1)
    visible_letter_2 = randint(0, len(word) - 1)
    masked_word = word
    while visible_letter_1 == visible_letter_2:
        visible_letter_2 = randint(1, len(word))
    for i in range(len(word)):
        if i != visible_letter_1 and i != visible_letter_2:
            masked_word = masked_word[:i] + "_" + masked_word[i + 1:]
    return word, masked_word
