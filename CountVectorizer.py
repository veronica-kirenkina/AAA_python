from typing import List


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
    wordcount : list
        массив из списков с количеством появлений каждого слова

    Methods
    -------
    fit_transform(array_of_strings)
        Выводит список уникальных слов из предложенного массива
    get_feature_names()
        Выводит массив из списков с количеством появлений каждого слова
    """

    def __init__(self):
        self.uniquewords = []
        self.wordcount = []

    def fit_transform(self, array_of_strings: List[str]) -> List[int]:
        """
        Считывает массив из строк и выводит терм-документную матрицу для каждой строки из массива

        Parameters
        ----------
        array_of_strings : list
            массив строк
        """
        uniquewords = []
        for j in array_of_strings:
            for i in j.lower().split():
                if i not in uniquewords:
                    uniquewords.append(i)
        self.uniquewords = uniquewords
        wordcount = []
        for j in array_of_strings:
            result = {}
            for i in uniquewords:
                result[i] = j.lower().count(i)
            wordcount.append(list(result.values()))
        self.wordcount = wordcount
        return self.wordcount

    def get_feature_names(self) -> List[str]:
        """Выводит массив из списков с количеством появлений каждого слова"""
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
