class CountVectorizer:
    """
    Класс CountVectorizer используется для разбивки текста на слова.
    Он удаляет знаки препинания и преобразует все слова в нижний регистр.
    Формируется словарь известных слов, который также используется
    для последующего кодирования текста.
    Возвращается закодированный вектор длиной количества уникальных слов
    и целым числом количества раз, когда каждое слово появлялось.

    Attributes
    ----------
    uniquewords : list
        список из уникальных слов в предложенном массиве
    wordcount : list[list]
        массив из списков с количеством появлений каждого слова

    Methods
    -------
    fit_transform(array_of_strings)
        Выводит массив из документов с количеством появлений каждого слова в документе
    get_feature_names()
        Выводит список уникальных слов из предложенного массива
    """

    def __init__(self):
        self.uniquewords = []
        self.wordcount = []

    def fit_transform(self, array_of_strings: list[str]) -> list[list[int]]:
        """
        Считывает массив из строк и выводит терм-документный вектор
        для каждой строки из массив. На выходе получается терм-документная матрица.

        Parameters
        ----------
        array_of_strings : list
            массив строк
        """
        for string in array_of_strings:
            for word in string.lower().split():
                if word not in self.uniquewords:
                    self.uniquewords.append(word)

        for string in array_of_strings:
            result = []
            for word in self.uniquewords:
                result.append(string.lower().count(word))
            self.wordcount.append(result)

        return self.wordcount

    def get_feature_names(self) -> list[str]:
        """
        Выводит массив уникальных слов,
        встречающихся хотя бы в одном документе из предложенного массива
        """
        return self.uniquewords


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
