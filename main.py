# coding: utf-8
from random import choice, randint
from json import loads

def start_game() -> bool:
    """
    Функция предлагает сыграть в игру
    :return is_quit_game: указатель отказа от игры
    """
    wanna_play = input("Сыграем в игру? (да / нет): ")
    if wanna_play.upper() in {"ДА", "Д", "YES", "Y"}:
        is_quit_game = False
    else:
        is_quit_game = True
    return is_quit_game


def read_words_file(*, file_name) -> list[str]:
    """
    Функция считывает слова длинее 6 букв из текстового файла
    и добоавляет их в список слов для игры
    :param file_name: файл со словами
    :return words_list: список слов для игры
    """
    words_list = []
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            if len(line) > 6:
                words_list.append(line[:-1])
    return words_list


def read_ascii_file(*, file_name) -> dict[str:str]:
    """
    Функция считывает ascii - картинки из .json файла и добавляет в словарь
    :param file_name: файл с ascii - картинками
    :return: словарь с ascii - картинками для изображения виселицы и человечка
    """
    with open(file_name, "r") as json_file:
        json_string = json_file.read()
        loaded_dict = loads(json_string)
    return loaded_dict


def choose_word(*, words_list) -> str:
    '''
    Функция загадывает слово для текущей игры
    :param words_list: множество слов для игры
    :return: - загаданное слово
    '''
    word = choice(words_list).upper()
    return word


def mask_word(*, word) -> str:
    """
    Функция маскирует в указанном слове все буквы кроме двух
    :param word: выбранное слово
    :return: маскированное слово
    """
    displayed_item_1 = randint(0, len(word) - 1)
    displayed_item_2 = randint(0, len(word) - 1)
    hidden_word = word
    while displayed_item_1 == displayed_item_2 or word[displayed_item_1] == word[displayed_item_2]:
        displayed_item_2 = randint(1, len(word))
    for i in range(len(word)):
        if i != displayed_item_1 and i != displayed_item_2:
            hidden_word = hidden_word[:i] + "_" + hidden_word[i + 1:]
    return hidden_word


def draw_hangman(img_dict, mistakes):
    """ Функция выводит изображение виселицы и человечка """
    if mistakes < 6:
        print(img_dict[str(mistakes)], end="")
    else:
        print(img_dict["6"], end="")


def read_char(word, masked_word, mistakes_number, wrong_letters, right_letters, is_victory, is_defeat) -> tuple:
    """
    Функция считывает символ с клавиатуры. Проверяет что это буква русского алфавита.
    Если буква есть в загаданном слове, то добавляет букву в множество правильных ответов
    и открывает его в замаскированном слове.
    Если в загаданном слове нет такой буквы, то она добавляется в множество неправильных
    ответов и число ошибок увеличивается на единицу.
    Если в загаданном слове отгаданы все буквы игрок победил.
    Если ошибок больше пяти, то игрок проиграл.
    :param mistakes_number: количество ошибок
    :param wrong_letters: множество неправильных ответов
    :param right_letters: множество правильных ответов
    :param is_victory: указатель победы
    :param is_defeat: указатель поражения
    """
    CYRILLIC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-"
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {wrong_letters if wrong_letters else ""}")
    letter = input(f"Слово: {masked_word}. Назовите букву: ")
    while not letter.upper() in CYRILLIC:
        letter = input("Допускаются только буквы русского алфавита. Назовите букву: ")
    letter = letter.upper()
    if letter in word:
        right_letters.add(letter)
        for index, value in enumerate(word):
            if value in letter:
                masked_word = (masked_word[:index] + letter + masked_word[index + 1:])
        if masked_word == word:
            is_victory = True
    else:
        if not letter in wrong_letters:
            wrong_letters.add(letter)
            mistakes_number += 1
        if mistakes_number > 5:
            is_defeat = True
    return (masked_word, mistakes_number, wrong_letters, right_letters, is_victory, is_defeat)


def report_victory(ascii_dict, mistakes_number, wrong_letters, mystery_word):
    """ Функция поздравляет с победой """
    draw_hangman(img_dict=ascii_dict, mistakes=mistakes_number)
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {wrong_letters if wrong_letters else ""}")
    print(f"Слово: {mystery_word}! Миссия выполнена!")


def report_defeat(ascii_dict, mistakes_number, wrong_letters, mystery_word):
    """ Функция уведомляет о поражении """
    draw_hangman(img_dict=ascii_dict, mistakes=6)
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {wrong_letters if wrong_letters else ""}")
    print(f"Слово: {mystery_word}! Миссия провалена!")


def play_again() -> bool:
    """
    Функция предлагает сыграть еще раз
    :return: указатель выхода из игры
    """
    wanna_play = input("Сыграем еще раз? (да / нет): ")
    if wanna_play.upper() in {"ДА", "Д", "YES", "Y"}:
        is_quit_game = False
    else:
        is_quit_game = True
    return is_quit_game


def play_game(words, ascii_dict) -> bool:
    """
    Функция загадывает слово и запрашивает буквы, до победы или поражения.
    После предлагает сыграть еще раз.
    :param words: множество слов для игры
    :param ascii_dict: словарь с ascii - картинками
    """
    mystery_word = choose_word(words_list=words)
    masked_word = mask_word(word=mystery_word)
    mistakes_number = 0
    wrong_letters, right_letters = set(), set()
    is_victory, is_defeat = False, False
    while not is_victory and not is_defeat:
        draw_hangman(img_dict=ascii_dict, mistakes=mistakes_number)
        masked_word, mistakes_number, wrong_letters, right_letters, is_victory, is_defeat\
            = read_char(mystery_word, masked_word, mistakes_number, wrong_letters, right_letters, is_victory, is_defeat)
    if is_victory:
        report_victory(ascii_dict, mistakes_number, wrong_letters, mystery_word)
    if is_defeat:
        report_defeat(ascii_dict, mistakes_number, wrong_letters, mystery_word)
    is_game_over = play_again()
    return is_game_over


def say_good_bye():
    """ Функция прощается с игроком """
    print("До свидания! Будем ждать вас в игре!")


def main():
    is_game_over = start_game()
    if not is_game_over:
        words = read_words_file(file_name="russian_nouns.txt")
        ascii_dict = read_ascii_file(file_name="ascii.json")
        while not is_game_over:
            is_game_over = play_game(words=words, ascii_dict=ascii_dict)
    say_good_bye()


if __name__ == "__main__":
    main()