# HW2


Код для получения артефактов всех задач [тут](solve_tasks.py)

## Easy
Функции для получения таблицы/визуализации в латехе [тут](latex.py). 

[Tex-файл с таблицей](artifacts/easy_table.tex)

## Medium

Ссылка на пакет - https://test.pypi.org/project/hw1-pestova/

[PDF с таблицей и графом](artifacts/medium_table.pdf)

## Hard

[Dockerfile](Dockerfile)

Build image:
 
```sh
docker build . -t hw2 --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g)
```

Для получения всех артефактов в докере запустить в текущей папке:

```sh
docker run -v "$(pwd)":/workspace/hw2/ hw2 /bin/bash -c \
    "cd hw2 && python3 solve_tasks.py && \
    cd artifacts && pdflatex medium_table.tex && \
    rm medium_table.aux && rm medium_table.log"
```

После этого в папке artifacts появятся все артефакты (для easy и medium тоже). 
