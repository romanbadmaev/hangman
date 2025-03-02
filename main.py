from words import guess_word
from ascii import draw_hangman

game_over = False # условие выхода из игры
victory = False # победа в игре
fiasco = False # поражение в игре
word, masked_word = guess_word()
mistakes_number = 0 # количество ошибок
wrong_letters = set() # множество неправильных ответов
right_letters = set() # множество правильных ответов

cyrillic = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-" # буквы русского алфавита

def play_game(*,
    word:str="Виселица",
    masked_word:str="В______а",
    mistakes_number:int=0,
    wrong_letters:set=set(),
    right_letters:set=set(),
    victory:bool=False,
    fiasco:bool=False):
    """
    загадывание слова
    :param word:
    :param masked_word:
    :param mistakes_number:
    :param wrong_letters:
    :param right_letters:
    :param victory:
    :param fiasco:
    :return:
    """
    draw_hangman(mistakes=mistakes_number)
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {wrong_letters if wrong_letters else ""}")
    letter = input(f"Слово: {masked_word}. Назовите букву: ") # ввод буквы - ответа:
    while not letter.upper() in cyrillic: # проверка корректности вводимых символов
        letter = input("Допускаются только буквы русского алфавита. Назовите букву: ")
    letter = letter.upper()
    if letter in word: # есть ли в загаданном слове введенная буква
        right_letters.add(letter)
        for index, value in enumerate(word):
            if value in letter:
                masked_word = (masked_word[:index] + letter + masked_word[index + 1:])
        if masked_word == word:
            victory = True
    else:
        if not letter in wrong_letters:
            wrong_letters.add(letter)
            mistakes_number += 1
        if mistakes_number > 5:
            fiasco = True
    return (
        masked_word,
        mistakes_number,
        wrong_letters,
        right_letters,
        victory,
        fiasco)

draw_hangman(mistakes=0) # заставка
# запуск и перезапуск игры
while not game_over:
    print("Сыграем в игру?")
    print("Напишите (да / нет): ", end="")
    play_again = input()
    if play_again.upper() in ["ДА", "Д", "YES", "Y"]:
        word, masked_word = guess_word()
        victory, fiasco = False, False
        mistakes_number = 0
        wrong_letters = set()
        right_letters = set()
        while not victory and not fiasco:
            masked_word,
            mistakes_number,
            wrong_letters,
            right_letters,
            victory,
            fiasco = play_game(
                word=word,
                masked_word=masked_word,
                mistakes_number=mistakes_number,
                wrong_letters=wrong_letters,
                right_letters=right_letters,
                victory=victory,
                fiasco=fiasco)
        else:
            draw_hangman(mistakes=mistakes_number)
            print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {
            wrong_letters if wrong_letters else ""}")
            if victory:
                print(f"Слово: {masked_word}! Миссия выполнена!")
            if fiasco:
                print(f"Слово: {word}. Миссия провалена!")
    else:
        print("До новых встреч!")
        game_over = True