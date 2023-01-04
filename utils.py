import requests
import random
from basic_word import BasicWord


def load_random_word(path):
    """
    Получает список слов с внешнего ресурса.
    Выбирает случайное слово.
    Создает экземпляр класса BasicWord.
    :return: Созданный экземпляр класса.
    """

    response = requests.get(path)
    words = response.json()
    word = random.sample(words, 1)[0]
    basic_word = BasicWord(word["word"], word["subwords"])

    return basic_word
