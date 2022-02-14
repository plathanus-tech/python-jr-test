# Create here the NodeManager Class
from typing import List
import nodes.node

T = List[nodes.node.Node]


class NodeManager:
    nodes: T
    node: object

    def __init__(self, nodes: T):
        if not isinstance(nodes, List):
            raise ValueError('NodeManager must receive an list of Node to be instanced')
        else:
            self.nodes: T = nodes.copy()

    def __len__(self) -> int:
        return len(self.nodes)

    def __getitem__(self, item) -> object:
        return self.nodes[item]

    def __repr__(self) -> str:
        return str([node_item.__repr__() for node_item in self.nodes])

    def remove(self, node: object) -> None:
        aux = [node_item.__repr__() for node_item in self.nodes]
        if node.__repr__() not in aux:
            raise ValueError("The given Node isn't in the list of Nodes")
        else:
            aux1 = []
            for item_index, node_item in enumerate(aux):
                if node_item == node.__repr__():
                    aux1.append(item_index)
            for node_index in aux1:
                del self.nodes[node_index]

    def remove_cascade(self, node: object) -> None:
        aux = [node_item.__repr__() for node_item in self.nodes]
        if node.__repr__() not in aux:
            raise ValueError("The given Node isn't in the list of Nodes")
        else:
            childrens_id = []
            aux1, removed_node = [], []
            for item_index, node_item in enumerate(aux):
                if node_item == node.__repr__():
                    aux1.append(item_index)
                elif node_item[-2] == node.__repr__()[5] or int(node_item[-2]) in childrens_id:
                    childrens_id.append(int(node_item[5]))
                    aux1.append(item_index)
                if node_item[-2] in childrens_id:
                    aux1.append(item_index)
            itens_to_remove = [self.nodes[i] for i in aux1]
            for node in itens_to_remove:
                self.nodes.remove(node)
