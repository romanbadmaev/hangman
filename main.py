# coding: utf-8
from random import choice, randint



def start_game():
    pass


def read_words_file():
    pass


def read_ascii_file():
    pass


def choose_word():
    pass


def mask_word():
    pass


def draw_hangman():
    pass


def read_char():
    pass


def report_victory():
    pass


def report_defeat():
    pass


def play_again():
    pass


def play_game(game_over):
    mystery_word = choose_word()
    masked_word = mask_word(mystery_word)
    while not is_victory and not is_defeat:
        draw_hangman()
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
        read_words_file()
        read_ascii_file()
        while not is_game_over:
            is_game_over = play_game()
    say_good_bye()


if __name__ == "__main__":
    main()