import numpy as np
from matrix import Matrix
from matrix_mixin import MixinMatrix
from hashed_matrix import HashedMatrix


def solve_easy():
    np.random.seed(0)

    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))

    with open("artifacts/easy/matrix+.txt", "w") as f:
        res = m1 + m2
        f.write(str(res))

    with open("artifacts/easy/matrix*.txt", "w") as f:
        res = m1 * m2
        f.write(str(res))

    with open("artifacts/easy/matrix@.txt", "w") as f:
        res = m1 @ m2
        f.write(str(res))


def solve_medium():
    np.random.seed(0)

    m1 = MixinMatrix(np.random.randint(0, 10, (10, 10)))
    m2 = MixinMatrix(np.random.randint(0, 10, (10, 10)))

    res = m1 + m2
    res.save("artifacts/medium/matrix+.txt")

    res = m1 * m2
    res.save("artifacts/medium/matrix*.txt")

    res = m1 @ m2
    res.save("artifacts/medium/matrix@.txt")


def solve_hard():
    # hash(A) = hash(C), так как имеют одинаковую сумму элементов
    A = HashedMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    C = HashedMatrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    # просто какая-то матрица
    B = HashedMatrix([[5, 4, 10], [9, -2, 45], [88, 0, 7]])
    D = HashedMatrix([[5, 4, 10], [9, -2, 45], [88, 0, 7]])

    with open("artifacts/hard/A.txt", "w") as f:
        f.write(str(A))

    with open("artifacts/hard/B.txt", "w") as f:
        f.write(str(B))

    with open("artifacts/hard/C.txt", "w") as f:
        f.write(str(C))

    with open("artifacts/hard/D.txt", "w") as f:
        f.write(str(D))

    assert A @ B == C @ D # из-за кэширования ок, однако понятно, что они не равны

    with open("artifacts/hard/AB.txt", "w") as f:
        AB = A @ B
        f.write(str(AB))

    # настоящий, незакэшированный результат
    with open("artifacts/hard/CD.txt", "w") as f:
        CD = C.__matmul__(D, cache=False)
        f.write(str(CD))

    assert AB != CD # не равны

    with open("artifacts/hard/hash.txt", "w") as f:
        res1 = hash(AB)
        res2 = hash(CD)
        f.write(str(res1) + '\n')
        f.write(str(res2) + '\n')


if __name__ == "__main__":
    solve_easy()
    solve_medium()
    solve_hard()
