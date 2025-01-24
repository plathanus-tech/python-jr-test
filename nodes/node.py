# Create here the Node Class


class Node:
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    id : int
        Identification key of the node
    parent : int
        Identification key of the node parent
    """

    id: int
    parent: int

    def __init__(self, id: int, parent: int) -> None:
        """
        Constructs all the necessary attributes for the node object

        Parameters
        ----------
            id : int
                Identification key of the node
            parent : int
                Identification key of the node parent
        """

        self.id = id
        self.parent = parent

        if not self.id and self.parent:
            raise ValueError("Id and parent is required")
        if not isinstance(self.id, int):
            raise ValueError("Id must be integer")
        if not isinstance(self.parent, int):
            raise ValueError("Parent must be integer")
        if self.id == self.parent:
            raise ValueError("Id cannot be equal to parent")
        if self.id < self.parent:
            raise ValueError("Id cannot be less than parent")

    def __repr__(self) -> str:
        return f"Node({self.id}, {self.parent})"
