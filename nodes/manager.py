from copy import copy
from typing import List

from nodes.node import Node


def is_valid_value(nodes) -> bool:
    is_node_type = isinstance(nodes, List)
    # is_sequence = ''

    if is_node_type:
        return True
    else:
        raise ValueError


class NodeManager:
    nodes: List[Node]

    def __init__(self, nodes: List[Node]):
        if is_valid_value(nodes):
            self.nodes = copy(nodes)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]

    def remove(self, node: Node):
        """
        Fiquei confuso nos testes desta função, porque em um teste é solicitado que não seja deletado por parâmetro,
        mas no outro teste é solcitado que seja. Logo não entendi como deveria ter feito
        :param node:
        :return:
        """
        return self.nodes.remove(node)

    def remove_cascade(self, node: Node):
        """
        Nesta função eu encontrei algumas maneiras de resolver,
        mas pensando em performance acredito que esta seja a melhor
        :param node:
        :return:
        """
        index = []
        for i, n in enumerate(self.nodes):
            if n.parent >= node.id:
                index.append(i)
        index.reverse()

        for i in index:
            self.nodes.pop(i)

        self.remove(node)
