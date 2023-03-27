import aiohttp
import asyncio
import aiofiles
import os
import time
import requests


async def get_photo(session, url):
    img = None
    async with session.get(url) as resp:
        if resp.status == 200:
            img = await resp.read()
    return img


async def save_photo(img, file):
    async with aiofiles.open(file, "wb") as f:
        await f.write(img)


async def async_load(url, path_to_save, n_img):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        load_tasks = [asyncio.create_task(get_photo(session, url)) for _ in range(n_img)]
        save_tasks = []

        for i, t in enumerate(asyncio.as_completed(load_tasks)):
            img = await t
            if img is not None:
                save_tasks.append(asyncio.create_task(save_photo(img, os.path.join(path_to_save, f"{i}.jpg"))))

    await asyncio.gather(*save_tasks)
    end_time = time.time()
    msg_result = f"Загружено {len(save_tasks)} картинок в папку {path_to_save} за {end_time-start_time:.2f}s."
    return msg_result


# функция для синхронного скачивания картинок для сравнения с асинхронной
def sync_load(url, path_to_save, n_img):
    start_time = time.time()
    n_res = 0
    for i in range(n_img):
        resp = requests.get(url)
        if resp.status_code == 200:
            img = resp.content
            with open(os.path.join(path_to_save, f"{i}.jpg"), "wb") as f:
                f.write(img)
                n_res += 1

    end_time = time.time()
    msg_result = f"Загружено {n_res} картинок в папку {path_to_save} за {end_time - start_time:.2f}s."
    return msg_result


if __name__ == "__main__":
    url = "https://picsum.photos/200/200"
    N = 100

    path_to_save = "artifacts/easy/img/"
    msg = asyncio.run(async_load(url, path_to_save, n_img=N))
    with open("artifacts/easy/easy.txt", "a", encoding="utf-8") as f:
        f.write("Асинхронное скачивание:\n")
        f.write(msg)
        f.write("\n")

    path_to_save = "artifacts/easy/sync_img/"
    msg = sync_load(url, path_to_save, n_img=N)
    with open("artifacts/easy/easy.txt", "a", encoding="utf-8") as f:
        f.write("Синхронное скачивание:\n")
        f.write(msg)
        f.write("\n")
