from nodes.node import Node
from typing import List

class NodeManager:
        """
        A class used to manage the Nodes

        Attributes
        ----------
        nodes : List
            list of Nodes
        """

    nodes: List[Node]

    def __init__(self, nodes: List[Node]):
        """
        Class constructor
        
        Makes sure that the type of the node object received is List, if it's not, raise an ValueError

        Parameters
        ----------
        nodes: List
        Receives a list of Nodes object and makes a copy of it to be managed by the class methods
        """

        if isinstance(nodes, List):
            self.nodes: List[Node] = nodes.copy()
        else:
            raise ValueError("Invalid parameter!")
    
    def __len__(self) -> int:
        """
        Return an int that represents the number of nodes in the nodes list

        Doesn't receive any parameter
        """

        return len(self.nodes)

    def __getitem__(self, index: int) -> Node:
        """
        Return an Node indexed by the index parameter

        Parameters
        ----------
        index : int
            The index used to search and return the Node desired
        """

        return self.nodes[index]

    def validate_node(self, node: Node):
        """
        Makes sure that the type of the node object received is Node, if it's not, raise an ValueError

        Parameters
        ----------
        node: Node
        node object of the class Node
        """

        if type(node) != Node:
            raise ValueError("Argument is not of the Node class")

    def remove(self, node: Node):
        """
        Removes only the desired Node from the node List

        Parameters
        ----------
        node: Node
        node object of the class Node
        """

        self.validate_node(node)
        self.nodes.remove(node)

    def remove_cascade(self, node: Node):
        """
        Removes the desired Node from the node List and its childrens (e.g.: all the Nodes that has the parent equal to the received Node id), it's a recursive method

        Parameters
        ----------
        node: Node
        node object of the class Node
        """

        self.validate_node(node)
        node_id = node.id
        self.nodes.remove(node)
        list_to_be_removed = []
        for n in self.nodes:
            if n.parent == node_id:
                list_to_be_removed.append(n)
        
        for n in list_to_be_removed:
            self.remove_cascade(n)