# Create here the NodeManager Class
from typing import List
from nodes.node import Node

class NodeManager:
    nodes: List[Node]

    def __init__(self, nodes:List[Node]) -> None:
        if not isinstance(nodes, list):
            raise ValueError("nodes must be a list of Node")

        self.nodes = nodes.copy()

    def __len__(self) -> int:
        return len(self.nodes)
    
    def __getitem__(self, index:int) -> Node:
        return self.nodes[index]
    
    def remove(self, node:Node) -> None:
        if node not in self.nodes:
            raise ValueError("node not found in nodes list")
        self.nodes.remove(node)

    def remove_cascade(self, node:Node) -> None:
        if node not in self.nodes:
            raise ValueError("node not found in nodes list")
        children = [n for n in self.nodes if n.parent == node.id]
        for child in children:
            self.remove_cascade(child)
        self.nodes.remove(node)