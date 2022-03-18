from typing import List
from .node import Node

# Create here the NodeManager Class

class NodeManager:
    nodes: List[Node] = []

    def __init__(self, nodes: List[Node]) -> None:
        if type(nodes) != list:
            raise ValueError('You must give a list of nodes for creating a node manager. You have passed an argument of type {} with value {}'.format(nodes.__class__.__name__, nodes))

        if len(nodes) == 0:
            raise ValueError('You must provide a list of nodes with at least 1 element of type Node. The list you have passed is empty')

        for node in nodes:
            if not isinstance(node, Node):
                raise ValueError('All elements from listt need to be an instance of Node')

        self.nodes = [n for n in nodes]

    def __len__(self) -> int:
        return len(self.nodes)

    def __getitem__(self, index: int):
        if index >= len(self.nodes) or index < 0:
            raise IndexError('index is out of range')

        return self.nodes[index]

    def remove(self, node: Node) -> None:
        if not isinstance(node, Node):
            raise ValueError('You must pass a node to be remove')

        if not node in self:
            raise ValueError('this node is not present in the manager')

        self.nodes.remove(node)

    def remove_cascade(self, node: Node) -> None:
        if not isinstance(node, Node):
            raise ValueError('You must pass a node to be remove')

        if not node in self:
            raise ValueError('this node is not present in the manager')

        children: List[Node] = [n for n in self.nodes if n.parent == node.id]
        for child in children:
            self.remove_cascade(child)

        self.remove(node)

