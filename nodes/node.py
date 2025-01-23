class Node:
    """
    Represents a single node in a hierarchical structure.

    Attributes:
        id (int): Unique identifier for the node.
        parent (int): Identifier of the parent node. Must be less than the node's id.
    """

    id: int
    parent: int

    def __init__(self, id: int, parent: int) -> None:
        """
        Initializes a Node object.

        Args:
            id (int): Unique identifier for the node.
            parent (int): Identifier of the parent node.

        Raises:
            ValueError: If the id or parent is invalid.
        """
        if not all(isinstance(x, int) for x in [id, parent]):
            raise ValueError("Both `id` and `parent` must be integers.")
        if parent >= id or id == parent:
            raise ValueError(
                "`parent` must be less than `id`, and `id` cannot equal `parent`."
            )

        self.id = id
        self.parent = parent

    def __repr__(self) -> str:
        """Returns a string representation of the Node."""
        return f"Node({self.id}, {self.parent})"
