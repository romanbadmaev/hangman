# прорисовка виселицы и человечка

hangman = {} # словарь с ascii картинками

#  добавляем картинки в словарь
for i in range(7):
    file_name = "hangman-" + str(i) + ".txt"
    file = open(file_name)
    ascii_string = ""
    for line in file:
        ascii_string += line
    hangman[i] = ascii_string

def draw_hangman(mistakes: int):
    """
    Прорисовка виселицы и человечка
    :param mistakes: кол-во ошибок
    """
    if mistakes < 6:
        print(hangman[mistakes], end="")
    else:
        print(hangman[6], end="")