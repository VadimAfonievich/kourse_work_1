class Player:
    def __init__(self, user_name, used_words):
        self.user_name = user_name
        self.used_words = []

    def add_used_words(self, user_answer):
        """
        Добавляет слова в использованные слова.
        :return: ничего
        """
        self.used_words.append(user_answer)

    def get_number_used_words(self):
        """
        Получает количество использованных слов.
        :return: int()
        """
        return int(len(self.used_words))

    def check_using_word_before(self, user_answer):
        """
        Проверяет использование данного слова ранее.
        :return: bool
        """
        if user_answer in self.used_words:
            return True

    def __repr__(self):
        return f"Пользователь: {self.user_name}\n" \
               f"Использованные слова: {self.used_words}"
