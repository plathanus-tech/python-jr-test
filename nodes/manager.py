# Create here the NodeManager Class

# class NodeManager:
#     pass


from typing import List
from nodes.node import Node 

class NodeManager:
    nodes: List[Node]

    def __init__(self, nodes: List[Node]):
        if not isinstance(nodes, list) or any(not isinstance(node, Node) for node in nodes):
            #Garante que o node é uma lista.
            #OBS: Foi feito a validação de cada um dos elementos da lista sejam uma instancia de Node
            raise ValueError("Nodes must be a list of 'Node instances'.")
        #Copia a lista fornecida
        self.nodes = nodes.copy() 

    def __len__(self):
        # retorna o número de elementos do Node
        return len(self.nodes)

    def __getitem__(self, index):
        #obtem um objeto Node na posição index da lista
        return self.nodes[index]

    def remove(self, node: Node):
        if node not in self.nodes:
            #valida se o node a ser removido existe na lista
            raise ValueError("Node does not exist in the list.")
        #retorna a remoção do node (None)
        return self.nodes.remove(node)


    #OBS: Foram feitas duas logicas para o remove cascade:
    #1: onde a lógica de remover os filhos e netos seja integrada a função (requerido pelo exercício)
    #2: onde a lógica do cascade foi separada em uma função a parte
    #para motivos de avaliação foi mantido os dois métodos 


    #1:
    
    def remove_cascade(self, node: Node):
        if node not in self.nodes:
            #valida se o node existe na lista
            raise ValueError("Node does not exist in the list.")
        children = [n for n in self.nodes if n.parent == node.id]
        for child in children:
            self.remove_cascade(child)
        self.nodes.remove(node)
        #Chama a logica de remoção dos parentes
        

    #2:

    # def remove_cascade(self, node: Node):
    #     if node not in self.nodes:
    #         #valida se o node existe na lista
    #         raise ValueError("Node does not exist in the list.")
    #     #Chama a logica de remoção dos parentes
    #     self._remove_cascade_recursive(node)

    # def _remove_cascade_recursive(self, node: Node):
    #     #lista de Nodes que possuem o id como parent.
    #     children = [n for n in self.nodes if n.parent == node.id]
    #     #Para cada children, 
    #     # é chamada a _remove_cascade_recursive recursivamente 
    #     # para remover os netos.
    #     for child in children:
    #         self._remove_cascade_recursive(child)
    #     self.nodes.remove(node)