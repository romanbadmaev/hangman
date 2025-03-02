# coding: utf-8
from random import choice, randint

def get_words_list(*, file_name: str) -> list:
    """
    Cоздание списка слов для игры из текстового файла
    :param file_name: имя текстового файла
    :return: список слов для игры
    """
    words = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            if len(line) > 6:
                words.append(line[:-1])
    return words


def guess_word() -> tuple[str, str]:
    '''
    функция которая загадывает слово для текущей игры и маскирует его
    :return: word - загаданное слово
             masked_word - загаданное слово, где замаскированны все буквы кроме двух
    '''
    word = choice(words).upper()
    displayed_item_1 = randint(0, len(word) - 1)
    displayed_item_2 = randint(0, len(word) - 1)
    masked_word = word
    while displayed_item_1 == displayed_item_2:
        displayed_item_2 = randint(1, len(word))
    for i in range(len(word)):
        if i != displayed_item_1 and i != displayed_item_2:
            masked_word = masked_word[:i] + "_" + masked_word[i + 1:]
    return word, masked_word


words = get_words_list(file_name="russian_nouns.txt")