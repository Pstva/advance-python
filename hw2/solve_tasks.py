from latex import make_document, make_table, make_vis
from hw1_pestova import AST, fib


def make_easy_artefacts():
    some_data = [["col1", "col2", "col3", "col4"], [1, 2, 3, 4], ["cat", "dog", "pig", "deer"]]
    table = make_table(some_data)
    doc = make_document([table])
    with open("artifacts/easy_table.tex", 'w') as f:
        f.write(doc)

def make_medium_artefacts():
    # creating visualization with my hw1_pestova package
    AST.draw_func_ast(fib.fib, "artifacts/ast_fib.png")
    # creating table
    some_data = [["col1", "col2", "col3", "col4"], [1, 2, 3, 4], ["cat", "dog", "pig", "deer"]]
    table = make_table(some_data)
    # creating tex-code for ast-graph
    vis = make_vis("ast_fib.png")
    doc = make_document([table, vis])
    with open("artifacts/medium_table.tex", 'w') as f:
        f.write(doc)



if __name__ == "__main__":
    make_easy_artefacts()
    make_medium_artefacts()