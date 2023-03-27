# HW5
## Easy
[Артефакты](artifacts/easy/):
+ [img](artifacts/easy/img/) - картинки, скачанные асинхронно 
+ [sync_img](artifacts/easy/sync_img/) - картинки, скачанные синхронно
+ [easy.txt](artifacts/easy/easy.txt/) - время выполнения асинхронной и синхронной функций скачивания и сохранения картинок

Скрипт: [easy.py](easy.py)

Прогоняла в докере:

Build:
```sh
docker build . -t hw5 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)
```

Run:
```sh
docker run -v "$(pwd)":/workspace/hw5/ hw5 /bin/bash -c "cd hw5 && python3 easy.py"
```
