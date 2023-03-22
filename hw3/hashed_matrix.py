from matrix import Matrix


class HashMixin:
    def __init__(self, matrix):
        self.matrix = matrix

    def __hash__(self):
        """
        Моя простая хэш-функция для двумерной матрицы - сумма всех значений, деленная на 3571
        :return: значение хеш-функции
        """
        return sum([sum(x) for x in self.matrix])


class HashedMatrix(Matrix, HashMixin):
    __cache = dict()

    def __matmul__(self, other, cache=True):
        others_hash = hash(other)
        self_hash = hash(self)
        # если используем кэш - ищем в нем пару хешей текущей матрицы и второй матрицы
        if cache is True:
            # если есть такая пара, отдаем результат
            if (self_hash, others_hash) in self.__cache:
                return self.__cache[(self_hash, others_hash)]
            if (others_hash, self_hash) in self.__cache:
                return self.__cache[(others_hash, self_hash)]
        # если не используем кэш или не нашли пару в нем, считаем сами, записываем в кэш, возвращаем
        self.__cache[(self_hash, others_hash)] = HashedMatrix(super().__matmul__(other))
        return self.__cache[(self_hash, others_hash)]
