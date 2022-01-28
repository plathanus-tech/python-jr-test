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
            self.nodes = nodes

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, item):
        return self.nodes[item]

    def remove(self, node: Node):
        return self.nodes.remove(node)

    def remove_cascade(self, node: Node):
        parent = set()

        for n in self.nodes:
            parent.add(n.parent)

        for node in self.nodes:
            if node.parent in parent:
                self.remove(node)
