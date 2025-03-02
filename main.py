# функция загадывания слов
from words import get_word
# функция прорисовки выселицы и человечка
from ascii import draw_hangman

game_over = False # условие выхода из игры
# строка с буквами русского алфавита
cyrillic = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-" # буквы русского алфавита

def play_game(*, word: str):
    """
    функция которая ведет игру
    :param word: загаданное слово
    :return:
    """
    global mistakes_number
    global wrong_letters
    global right_letters
    global masked_word
    global victory
    global fiasco

    draw_hangman(mistakes=mistakes_number)
    print(f"Ошибки: {mistakes_number} из 6. Неверные ответы: {
    wrong_letters if wrong_letters else ""}", )

    # ввод буквы - ответа:
    letter = input(f"Слово: {masked_word}. Назовите букву: ")
    while not letter.upper() in cyrillic:
        letter = input("Допускаются только буквы русского алфавита. Назовите букву: ")
    letter = letter.upper()

    # есть ли в загаданном слове введенная буква
    if letter in word:
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


# заставка
draw_hangman(mistakes=0)
# запуск и перезапуск игры
while not game_over:
    print("Сыграем в игру?")
    print("Напишите (да / нет): ", end="")
    play_again = input()
    if play_again.upper() in ["ДА", "Д", "YES", "Y"]:
        victory, fiasco = False, False
        word, masked_word = get_word()
        mistakes_number = 0
        wrong_letters = set()
        right_letters = set()
        while not victory and not fiasco:
            play_game(word=word)
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