# coding: utf-8
import json

def load_hangman_images(*, file_name: str) -> dict[str: str]:
    """
    загружаем из файла .json словарь с ascii - картинками виселицы
    :param file_name: - имя файла .json
    :return: словарь с ascii - картинками виселицы
    """
    with open(file_name, "r") as json_file:
        json_string = json_file.read()
        loaded_dict = json.loads(json_string)
    return loaded_dict


def draw_hangman(*, mistakes: int):
    """
    Прорисовка виселицы и человечка
    :param mistakes: кол-во ошибок
    """
    if mistakes < 6:
        print(hangman_images[str(mistakes)], end="")
    else:
        print(hangman_images["6"], end="")


hangman_images = load_hangman_images(file_name="ascii.json")