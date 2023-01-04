from utils import load_random_word
from player import Player


DATA_SOURCE = "https://www.jsonkeeper.com/b/AUOI"


def start_game():
    """
    Приветствует пользователя. Запускает цикл вопросов. Проверяет слова по условиям.
    """

    print("Программа: Введите имя игрока.")
    user_name = input("Пользователь: ")

    used_words = []
    player = Player(user_name, used_words)

    print(f"\nПрограмма: Привет, {user_name}!")

    basic_word = load_random_word(DATA_SOURCE)
    print(f"Программа: Составьте {basic_word.count_sub_words()} слов из слова '{basic_word.original_word.upper()}'\n"
          f"Программа: Слова должны быть не короче 3 букв\n"
          f"Программа: Чтобы закончить игру, угадайте все слова или напишите 'stop'!\n"
          f"Программа: Поехали, ваше первое слово?\n")

    while player.get_number_used_words() != basic_word.count_sub_words():
        user_answer = input("Пользователь: ")
        if len(user_answer) <= 2:
            print("Программа: Слишком короткое слово.")
        elif user_answer == "stop" or user_answer == "стоп":
            break
        elif not basic_word.is_correct(user_answer):
            print("неверно!")
        elif player.check_using_word_before(user_answer):
            print("Уже использовано!")
        else:
            print("Верно!")
            player.add_used_words(user_answer)


    print(f"Игра завершена, вы угадали {player.get_number_used_words()} слов "
          f"из {basic_word.count_sub_words()} возможных.!")


start_game()


# question_ = [{
#     "word": "питон",
#     "subwords": [
#         "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"
#     ]},
#     {
#     "word": "набор",
#     "subwords": [
#         "бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"
#     ]},
#     {
#     "word": "строка",
#     "subwords": [
#         "акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора",
#         "коса", "сота", "торс", "роса", "скат"
#     ]
# }]
