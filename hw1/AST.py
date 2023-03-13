import ast
import networkx as nx
import inspect
import fib
from networkx.drawing.nx_agraph import to_agraph


class ASTGraph:
    def __init__(self, ast_object):
        self.graph = nx.DiGraph()
        self.num_nodes = 0
        self.process_node(ast_object)

    def add_node(self, node, node_ind):
        """
        Добавляет AST ноду в граф.
        В зависимости от типа ноды добавляет название, цвет и форму ноды.
        :param node: нода AST
        :param node_ind: индекс ноды
        """
        # label = node.__class__.__name__
        label = str(type(node)).split(".")[-1][:-2]
        print(str(type(node)))
        color = "gray"
        style = "filled"
        shape = "box"
        arithm_operators = (ast.Add, ast.Mult, ast.Div, ast.Sub, ast.Eq, ast.LtE, ast.GtE)

        if isinstance(node, ast.Constant):
            label = f"{label} {node.value}"
            color = '#E8FF9B'
            shape = 'ellipse'
        elif isinstance(node, ast.Name):
            label = f"{label} {node.id}"
            color = '#6AF7AC'
            shape = 'circle'
        elif isinstance(node, (ast.Compare, ast.BinOp, ast.Assign)):
            color = '#E066BC'
            shape = 'rectangle'
        elif isinstance(node, arithm_operators):
            color = '#60C2FC'
            shape = 'square'
        elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
            shape = 'parallelogram'
            color = '#BEF8FA'
        elif isinstance(node, (ast.If, ast.For)):
            shape = 'diamond'
            color = '#E08C55'

        elif isinstance(node, (ast.Return, ast.Raise)):
            shape = 'trapezium'
            color = '#E06255'
        elif isinstance(node, ast.FunctionDef):
            shape = 'septagon'
            color = '#B36BFF'
        elif isinstance(node, ast.Call):
            label = f"{label} {node.func.id}"
            shape = 'egg'
            color = '#FFAFAD'

        self.graph.add_node(node_ind,
                            label=label,
                            color=color,
                            style=style,
                            shape=shape,
                            fontsize="30"
                            )

    def process_node(self, node, parent_ind=None):
        """
        Обрабатывает AST ноду и ее детей рекурснивно.
        :param node: нода AST
        :param parent_ind: индекс ноды-родителя
        """
        node_ind = self.num_nodes
        self.add_node(node, node_ind)
        if parent_ind is not None:
            self.graph.add_edge(parent_ind, node_ind)

        for child in ast.iter_child_nodes(node):
            self.num_nodes += 1
            self.process_node(child, node_ind)

    def draw(self, path):
        """
        Рисует граф с помощью Graphviz и сохраняет по данному пути.
        :param path: путь для сохранения графа
        """
        g = to_agraph(self.graph)
        g.layout()
        g.draw(path, prog="dot")


def draw_func_ast(func, path_to_save):
    """
    Парсит AST функции и изображает его на графе.
    :param func: функция для парсинга
    :param path_to_save: путь для сохранения графа
    """
    ast_object = ast.parse(inspect.getsource(func))
    graph = ASTGraph(ast_object)
    graph.draw(path_to_save)


if __name__ == "__main__":
    draw_func_ast(fib.fib, "artifacts/ast.png")

