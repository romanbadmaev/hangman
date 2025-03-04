# coding: utf-8
from random import choice, randint
from json import loads

def start_game() -> bool:
    """
    Функция предлагает сыграть в игру
    :return is_quit_game: указатель отказа от игры
    """
    wanna_play = input("Сыграем в игру? (да / нет): ")
    if wanna_play in {"ДА", "Д", "YES", "Y"}:
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
    while displayed_item_1 == displayed_item_2:
        displayed_item_2 = randint(1, len(word))
    for i in range(len(word)):
        if i != displayed_item_1 and i != displayed_item_2:
            hidden_word = hidden_word[:i] + "_" + hidden_word[i + 1:]
    return hidden_word


def draw_hangman(img_dict, mistakes):
    if mistakes < 6:
        print(img_dict[str(mistakes)], end="")
    else:
        print(img_dict["6"], end="")


def read_char():
    pass


def report_victory():
    pass


def report_defeat():
    pass


def play_again() -> bool:
    """
    Функция предлагает сыграть еще раз
    :return: указатель выхода из игры
    """
    wanna_play = input("Сыграем еще раз? (да / нет): ")
    if wanna_play in {"ДА", "Д", "YES", "Y"}:
        is_quit_game = False
    else:
        is_quit_game = True
    return is_quit_game

def play_game(is_game_over):
    mystery_word = choose_word(words_list=words)
    masked_word = mask_word(word=mystery_word)
    while not is_victory and not is_defeat:
        draw_hangman(img_dict=ascii_dict, mistakes=mistakes_number)
        read_char()
    if is_victory:
        report_victory()
    if is_defeat:
        report_defeat()
    is_game_over = play_again()

def say_good_bye():
    pass


def main():
    is_game_over = start_game()
    if not is_game_over:
        words = read_words_file(file_name="russian_nouns.txt")
        ascii_dict = read_ascii_file()
        while not is_game_over:
            is_game_over = play_game()
    say_good_bye()


if __name__ == "__main__":
    main()