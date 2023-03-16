def make_document(elements):
    """
    Создает валидный latex-документ, вставляя переданные latex-элементы
    :param elements: произвольное количество latex-элементов (строк), которые будут всталены в док-т в том же порядке
    :return: строка, представляющая latex-код документа
    """
    head = "\\documentclass{article}\n \\usepackage{graphicx}\n \\begin{document}\n"
    ending = "\\end{document}"
    full_text = head + "\n".join(elements) + ending
    return full_text


def make_table(data):
    """
    Создаем простую latex таблицу по данному списку списков.
    :param data: list of lists с данными для таблицы, где list[i] - i-строка таблицы
    :return: строка - код латеха
    """
    # проверим что дано одинаковое кол-во значений для колонок в каждой строке
    assert list(map(lambda x: len(x) == len(data[0]), data)), "Unequal number of values in rows"
    ncols = len(data[0])
    # шапка таблицы
    head = f"\\begin{{table}}[!htbp] \n\\centering \n\\small \n\\begin{{tabular}}{{|l|{'l|'*(ncols-1)}}} \n\\hline \n"
    # таблица
    table = ""
    for i, row in enumerate(data):
        row_str = " & ".join(list(map(str, row)))
        row_str += " \\\ \n"
        table += row_str
    # окончание таблицы
    end = "\\hline \\end{tabular} \n\\end{table}\n"
    return head + table + end


def make_vis(vis_path):
    """
    Генерирует латех код для вставки изображения в таблицу
    :param vis_path: путь до изображения
    :return: строка - код латеха
    """
    head = "\\begin{figure}\n"
    vis = f"\\includegraphics[width=\\textwidth]{{{vis_path}}}\n"
    ending = "\\end{figure}\n"
    return head + vis + ending
