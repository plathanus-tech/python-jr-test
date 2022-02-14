class Node:
        """
        A class used to define the structure of the Nodes

        Attributes
        ----------
        id : int
            the Node's id, it's unique 
        parent: int
            the Node's parent, e.g. parent is the id of an other Node
        """

    id: int
    parent: int

    def __init__(self, id: int, parent: int):
        """
        Class constructor
        
        Makes sure that the type of id and parent is int, if it's not, raise an ValueError
        Makes sure that the Node's parent isn't greater than or equal to the Node's id, if it's, raise an ValueError

        Parameters
        ----------
        id : int
            the Node's id, it's unique 
        parent: int
            the Node's parent, e.g. parent is the id of an other Node
        """
        if (not isinstance(id, int)) or (not isinstance(parent, int)):
            raise ValueError("Document Id and Document Parent should be integers!")
        elif parent >= id:
            raise ValueError("Parent can't be equal or greater than id!")
        self.id: int = id
        self.parent: int = parent

    def __repr__(self) -> str:
        """
        Makes sure that the representation of the Node is equal to the way it's instanced, return a string of its representation

        Doesn't receive any parameter
        """
        return "Node({},{})".format(self.id, self.parent)