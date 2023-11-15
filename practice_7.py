from typing import List
from math import log
from HW_3 import CountVectorizer

class TfidfTransformer:
    """
        Класс TfidfTransformer используется для оценки важности слова в контексте документа,
        являющегося частью коллекции документов или корпуса.

        Methods
        -------
        tf_transform(count_matrix)
            Выводит матрицу с подсчетом количества повторений слова к общему количеству слов в документе
        idf_transform(count_matrix)
            Выводит массив с подсчетом количества всех документов к документам, где встречается нужное слово
        fit_transform(count_matrix)
            Преобразуйте матрицу подсчета в нормализованное представление tf-idf
        """

    @staticmethod
    def tf_transform(count_matrix: List[int]) -> List[List[int]]:
        tf_matrix = []
        for doc in count_matrix:
            cnt_words = sum(doc)
            tf_vector = [round(word / cnt_words, 3) for word in doc]
            tf_matrix.append(tf_vector)
        return tf_matrix

    @staticmethod
    def idf_transform(count_matrix: List[int]) -> List[List[int]]:
        docs_len = len(count_matrix[0])
        cnt_docs = len(count_matrix)
        idf_matrix = []
        for word in range(docs_len):
            cnt_docs_with_word = 0
            for doc in count_matrix:
                if doc[word]:
                    cnt_docs_with_word += 1
            idf = round(log((cnt_docs + 1) / (cnt_docs_with_word + 1)) + 1, 3)
            idf_matrix.append(idf)

        return idf_matrix

    @classmethod
    def fit_transform(cls, count_matrix: List[int]) -> List[List[int]]:
        tf_idf_matrix = []
        for tf_vec in cls.tf_transform(count_matrix):
            tf_idf_matrix.append([round(i * j, 3) for i, j in zip(cls.idf_transform(count_matrix), tf_vec)])
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    """
        Класс TfidfTransformer используется для преобразования коллекции необработанных документов
        в матрицу объектов TF-IDF. Наследуется от класса CountVectorizer.

        Attributes
        ----------
        tfidf_transformer : TfidfTransformer
            экземпляр класса TfidfTransformer, необходимы для составления композиции

        Methods
        -------
        fit_transform(corpus)
            Возвращает матрицу применение tf-idf на корпусе документов
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        matrix = super().fit_transform(corpus)
        return self.tfidf_transformer.fit_transform(matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(transformer.tf_transform(count_matrix))
    print(transformer.idf_transform(count_matrix))
    print(tfidf_matrix)

    tf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tf_vectorizer.fit_transform(corpus)
    print(tf_vectorizer.get_feature_names())
    print(tfidf_matrix)
