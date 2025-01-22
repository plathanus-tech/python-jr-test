from .node import Node
from typing import List


class NodeManager:
    nodes: List[Node]

    def __init__(self, nodes: List[Node]):
        if not isinstance(nodes, list):
            raise ValueError("Must pass a list of nodes.")

        self.nodes = nodes.copy()
    

    def __getitem__(self, index) -> Node:
        return self.nodes[index]
    
    
    def __len__(self) -> int:
        return len(self.nodes)
    

    def remove(self, node: Node) -> None:
        index = self.nodes.index(node)
        self.nodes.pop(index)
    

    def remove_cascade(self, node: Node) -> None:
        index = self.nodes.index(node)
        stack = []
        stack.append(self.nodes.pop(index))
        while stack:
            node = stack.pop()
            to_remove = []
            for item  in self.nodes:
                if item.parent == node.id:
                    stack.append(item)
                    to_remove.append(item)
            for item in to_remove:
                self.nodes.remove(item)