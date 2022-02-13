
class Node:
    def __init__(self, id: int, parent: int):
        if (type(id) != int) or (type(parent) != int):
            raise ValueError("Document Id and Document Parent should be integers!")
        elif parent >= id:
            raise ValueError("Parent can't be equal or greater than id!")

        else:
            self.id: int = id
            self.parent: int = parent

    def __repr__(self) -> str:
        return "Node({},{})".format(self.id, self.parent)

if __name__ == "__main__":
    node1 = Node(1,0)
    node2 = Node(2,1)
    node3 = Node(3,1)
    node2 = Node(2,1)
    # node4 = Node(3,3)
