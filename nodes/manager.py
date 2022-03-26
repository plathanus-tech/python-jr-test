from typing import List

from nodes.node import Node


class NodeManager:

    def __init__(self, nodes: List[Node]):
        self.nodes = nodes[:]

    def __len__(self):
        return self.nodes.__len__()

    def __getitem__(self, item):
        return self.nodes[item]

    def remove(self, node: Node) -> None:
        self.__validate_node(node)
        self.nodes.remove(node)

    def remove_cascade(self, node: Node) -> None:
        self.__validate_node(node)

        deleted: List[Node] = [node]
        for node in deleted:
            for nd in self.nodes:
                if node.id == nd.parent:
                    deleted.append(nd)
            self.__remove_nodes(deleted)

    def __validate_node(self, node: Node) -> None:
        if node not in self.nodes:
            raise ValueError()

    def __remove_nodes(self, deleted: List[Node]):
        for nd in deleted:
            if nd in self.nodes:
                self.nodes.remove(nd)

