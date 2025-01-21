class Node:
    id: int  # Adding the type hint for the 'id' attribute
    parent: int  # Adding the type hint for the 'parent' attribute


    # Initializes the Node with id and parent, ensuring valid values.
    def __init__(self, id: int, parent: int):
        if not isinstance(id, int) or not isinstance(parent, int):
            raise ValueError("Both id and parent must be integers.")
        if parent >= id:
            raise ValueError("The parent cannot be greater than or equal to the id.")
		
        self.id: int = id
        self.parent: int = parent
		
    # Returns a string representation of the Node.
    def __repr__(self):
        return f"Node({self.id}, {self.parent})"
    
    # Compares two Nodes based on id and parent.
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id and self.parent == other.parent
        return False