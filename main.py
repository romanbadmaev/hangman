from words import guess_word
from ascii import draw_hangman

game_over = False # условие выхода из игры
mistakes_number = 0 # количество ошибок
wrong_letters = set() # множество неправильных ответов
right_letters = set() # множество правильных ответов
CYRILLIC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-" # буквы русского алфавита

def play_game(*,
    word:str, masked_word:str,
    mistakes_number:int=0,
    wrong_letters:set[str],
    right_letters:set[str]) ->tuple:
    """
    Функция выводит изображение виселицы, считывает и проверяет с клавиатуры букву. Если буква есть в
    загаданном слове, то сохраняет эту букву в множестве правильных ответов и открывает эту букву  в
    замаскированном слове. Если такой буквы нет, то добавляет букву в множество неправильных ответов и
    увеличивает на один количество ошибок.
    :param word: загаданное слово
    :param masked_word: замаскированное слово
    :param mistakes_number: количество ошибок
    :param wrong_letters: множество неправильных ответов
    :param right_letters: множество правильных ответов
    :return masked_word, mistakes_number, wrong_letters, right_letters:
    """
    draw_hangman(mistakes=mistakes_number)
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
    else:
        if not letter in wrong_letters:
            wrong_letters.add(letter)
            mistakes_number += 1
    return (masked_word, mistakes_number, wrong_letters, right_letters)


def get_result(mistakes_number:int, word:str, masked_word:str, wrong_letters: set[str]):
    """
    Функция выводит результат игры
    :param mistakes_number: количество ошибок
    :param word: загаданное слово
    :param masked_word: замаскированное загаданное слово
    :param wrong_letters: множество неправильных ответов
    """
    draw_hangman(mistakes=mistakes_number)
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {wrong_letters if wrong_letters else ""}")
    if masked_word == word:
        print(f"Слово: {masked_word}! Миссия выполнена!")
    if mistakes_number > 5:
        print(f"Слово: {word}. Миссия провалена!")


word, masked_word = guess_word() # загодали слово
draw_hangman(mistakes=0) # заставка
# запуск и перезапуск игры
while not game_over:
    print("Сыграем в игру?")
    play_again = input("Напишите (да / нет): ")
    if play_again.upper() in ["ДА", "Д", "YES", "Y"]:
        word, masked_word = guess_word()
        mistakes_number = 0
        wrong_letters = set()
        right_letters = set()
        while masked_word != word and mistakes_number < 6:
            masked_word, mistakes_number, wrong_letters, right_letters\
                = play_game(
                word=word,
                masked_word=masked_word,
                mistakes_number=mistakes_number,
                wrong_letters=wrong_letters,
                right_letters=right_letters)
        else:
            get_result(
                    mistakes_number=mistakes_number,
                    word=word, masked_word=masked_word,
                    wrong_letters=wrong_letters)
    else:
        print("До новых встреч!")
        game_over = True