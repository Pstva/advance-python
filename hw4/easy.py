from threading import Thread
from multiprocessing import Process
import timeit
import numpy as np


def fib(n):
    # первые элементы
    l, r = 0, 1
    # n=0 и n=1 - особые случаи
    if n <= 0:
        raise ValueError('Число Фиббоначи определено только для натуральных чисел')
    if n == 1:
        return 0
    if n == 2:
        return 1
    # циклом обновляем предыдущий и текущий элементы
    for _ in range(3, n + 1):
        l, r = r, l + r
    return r


def make_n_jobs(func, args, worker=Thread, n_jobs=10):
    threads = []
    for i in range(n_jobs):
        t = worker(target=func, args=args)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return


def make_n_sync(func, args, n):
    for i in range(n):
        func(*args)
    return


def time_exec(func, number):
    result = timeit.repeat(func, number=number)
    return np.mean(result), np.std(result)


if __name__ == "__main__":
    n_fib = 30000
    n_runs = 50
    n_jobs = 10

    with open("artifacts/easy.txt", "w") as f:
        f.write(f"func: fib({n_fib}), n_jobs={n_jobs}, n_runs={n_runs}\n")
        f.write("Синхронное выполнение: ")
        m, s = time_exec(lambda: make_n_sync(fib, (n_fib,), n=n_jobs), number=n_runs)
        f.write(f"mean={m:.4f}s, std={s:.4f}s\n")
        f.write("Мультипоточное выполнение: ")
        m, s = time_exec(lambda: make_n_jobs(fib, (n_fib,), worker=Thread, n_jobs=n_jobs), number=n_runs)
        f.write(f"mean={m:.4f}s, std={s:.4f}s\n")
        f.write("Мультипроцессорное выполнение: ")
        m, s = time_exec(lambda: make_n_jobs(fib, (n_fib,), worker=Process, n_jobs=n_jobs), number=n_runs)
        f.write(f"mean={m:.4f}s, std={s:.4f}s\n")
