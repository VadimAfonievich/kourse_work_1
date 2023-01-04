class BasicWord:
    def __init__(self, original_word, valid_sub_words):
        self.original_word = original_word
        self.valid_sub_words = valid_sub_words

    def is_correct(self, user_answer):
        """
        Проверяет введенное слово в списке допустимых слов.
        :return: bool
        """
        if user_answer.lower() in self.valid_sub_words:
            return True

    def count_sub_words(self):
        """
        Подсчитывает количество подслов.
        :return:
        """

        return int(len(self.valid_sub_words))

    def __repr__(self):
        return f"Слово: '{self.original_word}'\n" \
               f"Подслова: {self.valid_sub_words}"
