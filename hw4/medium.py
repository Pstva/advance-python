import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os
from timeit import timeit
import logging
import pandas as pd
import matplotlib.pyplot as plt


def integration_step(args):
    f, f_arg, logger = args
    if logger is not None:
        logger.info(f"running integration step: f({f_arg})")
    return f(f_arg)


def integrate(f, a, b, *, worker=ThreadPoolExecutor, n_jobs=1, n_iter=1000, logger=None):
    step = (b - a) / n_iter
    with worker(max_workers=n_jobs) as executor:
        # runs n_iter tasks concurrently
        futures = executor.map(integration_step, [(f, a + i * step, logger) for i in range(n_iter)])
    # sum up results
    return sum(list(futures)) * step


def run_integrate_experiments(logger_path):
    # создаем логгер
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(threadName)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        filename=logger_path
    )
    logger = logging.getLogger(__name__)
    data = []
    for work in [ThreadPoolExecutor, ProcessPoolExecutor]:
        for n_jobs in range(1, os.cpu_count() * 2 + 1): # 12 cpu на моем ноутбуке
            logger.info(f"starting integration with {work.__name__} and n_jobs={n_jobs}")
            time = timeit(lambda: integrate(math.cos, 0, math.pi / 2, worker=work, n_jobs=n_jobs, logger=logger), number=1)
            data.append([work.__name__, n_jobs, time])

    return data


def save_results(data, table_path, vis_path):
    data = pd.DataFrame(data, columns=["executor", "n_jobs", "time"])

    df = data.pivot(index='n_jobs', columns='executor', values='time').reset_index()
    df.to_csv(table_path, index=False)

    plt.plot(df['n_jobs'], df['ThreadPoolExecutor'], label='ThreadPoolExecutor', c='red')
    plt.plot(df['n_jobs'], df['ProcessPoolExecutor'], label='ProcessPoolExecutor', c='blue')
    plt.title("Время выполнения функции интеграции")
    plt.xlabel("#jobs")
    plt.ylabel("время (сек)")
    plt.legend()
    plt.savefig(vis_path)


if __name__ == "__main__":
    results = run_integrate_experiments(logger_path="artifacts/medium/logs.txt")
    save_results(results, "artifacts/medium/table.csv", "artifacts/medium/viz.png")
