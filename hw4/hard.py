import codecs
from multiprocessing import Queue, Process
import logging
import time


def a(in_queue, out_queue, logger):
    while True:
        s = in_queue.get()
        logger.info(f"Процесс A принял строку {s}")
        s = s.lower()
        time.sleep(5)
        logger.info(f"Процесс A отдал строку {s}")
        out_queue.put(s)


def b(in_queue, out_queue, logger):
    while True:
        s = in_queue.get()
        logger.info(f"Процесс B принял строку {s}")
        encoded = codecs.encode(s, 'rot_13')
        logger.info(f"Процесс B отдал строку {encoded} ({s})")
        out_queue.put(encoded)


def main(logger):
    main_queue, a_queue, b_queue = Queue(maxsize=20), Queue(maxsize=20), Queue(maxsize=20)
    A = Process(target=a, args=(main_queue, a_queue, logger), daemon=True)
    B = Process(target=b, args=(a_queue, b_queue, logger), daemon=True)
    A.start()
    B.start()

    while True:
        data = input()
        if 'Exit' == data:
            logger.info("exited")
            return
        if data:
            logger.info(f"stdin: {data}")
            main_queue.put(data)
        while not b_queue.empty():
            s = b_queue.get()
            logger.info(f"stdout: {s})")
            print(s)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        filename="artifacts/hard_log.txt"
    )
    logger = logging.getLogger(__name__)
    main(logger)
