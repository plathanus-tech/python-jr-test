# Create here the NodeManager Class
from typing import List, Optional
import nodes.node

T = List[nodes.node.Node]
T1 = 'Optional[nodes.node.Node]'


class NodeManager:
    nodes: T
    node: T1

    def __init__(self, nodes: T):
        if not isinstance(nodes, List):
            raise ValueError('NodeManager must receive an list of Node to be instanced')
        else:
            self.nodes: T = nodes.copy()

    def __len__(self) -> int:
        return len(self.nodes)

    def __getitem__(self, item) -> T1:
        return self.nodes[item]

    def __repr__(self) -> str:
        return str([item for item in self.nodes])

    def remove(self, node: T1) -> None:
        if node not in self.nodes:
            raise ValueError("The given Node isn't in the list of Nodes")
        else:
            self.nodes.remove(node)

    def remove_cascade(self, node: T1) -> None:
        childrens = [item for item in self.nodes if node.id == item.parent]
        self.remove(node)
        for item in childrens:
            self.remove_cascade(item)
