# Create here the Node Class


# class Node:
#     pass


class Node:
    id: int
    parent: int

    def __init__(self, id: int, parent: int):

        if not isinstance(id, int) or not isinstance(parent, int):
            #validação dupla de instancia para id e parent.
            raise ValueError("Node class init raises given non integer.")
        
        if parent > id:
            # validação se o parent é maior que o id. 
            # OBS poderia ser usado o >= para validar se é maior ou iqual,
            # mas foi optado separar as validações por motivos didaticos 
            raise ValueError("Node does not accept PARENT greater than children.")
        
        if parent == id:
            # validação se o parent é iqual ao id.
            raise ValueError("Node does not accept ID as PARENT of itself.")
        
        self.id = id
        self.parent = parent

    def __repr__(self):
        return f"Node({self.id}, {self.parent})"
