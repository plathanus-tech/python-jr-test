# Create here the NodeManager Class
from typing import List

from nodes.node import Node


class NodeManager:
    """
    A class to represent a manager of the nodes object.

    ...

    Attributes
    ----------
    nodes : List[Node]
        List of the nodes

    Methods
    -------
    remove(elem: Node):
        Remove a node
    remove_cascade(elem: Node):
        Remove a node with its parents
    """

    nodes: List[Node]

    def __init__(self, nodes: List[Node]) -> None:
        """
        Constructs all the necessary attributes for the node manager object

        Parameters
        ----------
            nodes : List[Node]
                List of the nodes object
        """

        if not isinstance(nodes, list):
            raise ValueError("Needs a list of Node object to instance it")

        self.nodes = nodes.copy()

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, key):
        return self.nodes[key]

    def remove(self, elem: Node) -> None:
        """
        Remove a node object

        Parameters
        ----------
        elem : Node
            Node object

        Returns
        -------
        None
        """
        self.nodes.remove(elem)

    def remove_cascade(self, elem: Node) -> None:
        """
        Remove a node object with its parents

        Parameters
        ----------
        elem : Node
            Node object

        Returns
        -------
        None
        """

        # parents = [elem.id]
        # items_to_delete = [elem]
        # for item in self.nodes:
        #     if item.parent in parents:
        #         parents.append(item.id)
        #         items_to_delete.append(item)
        #
        # [self.remove(item) for item in items_to_delete[::-1]]

        parents = [item for item in self.nodes if item.parent == elem.id]
        for item in parents:
            self.remove_cascade(item)
        else:
            self.remove(elem)
