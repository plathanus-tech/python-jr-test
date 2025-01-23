from typing import Dict, List

from nodes.node import Node


class NodeManager:
    """
    Manages a collection of Node objects, providing functionality to remove nodes
    and cascade their removal through children.

    Attributes:
        nodes (List[Node]): A list of Node objects managed by this instance.
        _children_map (Dict[int, List[Node]]): A mapping of parent IDs to their child nodes.
    """

    nodes: List[Node]

    def __init__(self, nodes: List[Node]) -> None:
        """
        Initializes the NodeManager with a list of nodes.

        Args:
            nodes (List[Node]): A list of Node objects.

        Raises:
            ValueError: If `nodes` is not a list or contains non-Node elements.
        """
        if not isinstance(nodes, list) or not all(
            isinstance(node, Node) for node in nodes
        ):
            raise ValueError("`nodes` must be a list of Node instances.")

        self.nodes = nodes.copy()
        self._children_map = self._build_children_map()

    def _build_children_map(self) -> Dict[int, List[Node]]:
        """
        Builds a map of parent IDs to their children to reduce repetitive searches and increase performance.

        Returns:
            Dict[int, List[Node]]: A mapping of parent IDs to their child nodes.
        """
        children_map = {}
        for node in self.nodes:
            if node.parent not in children_map:
                children_map[node.parent] = []
            children_map[node.parent].append(node)
        return children_map

    def __len__(self) -> int:
        """Returns the number of nodes managed."""
        return len(self.nodes)

    def __getitem__(self, pos: int) -> Node:
        """Allows access to nodes by index."""
        return self.nodes[pos]

    def remove(self, node: Node) -> None:
        """
        Removes a node from the manager.

        Args:
            node (Node): The node to remove.

        Raises:
            ValueError: If the node is not found.
        """
        if node not in self.nodes:
            raise ValueError("Node not found in the manager.")

        self.nodes.remove(node)
        self._children_map = self._build_children_map()

    def remove_cascade(self, node: Node) -> None:
        """
        Removes a node and all its descendants recursively.

        Args:
            node (Node): The node to remove along with its descendants.

        Raises:
            ValueError: If the node is not found.
        """
        if node not in self.nodes:
            raise ValueError("Node not found in the manager.")

        # Abordagem baseada em pilha para evitar problemas de profundidade de recursão
        stack = [node]
        while stack:
            current_node = stack.pop()
            stack.extend(self._children_map.get(current_node.id, []))
            self.remove(current_node)
