from typing import List
from nodes.node import Node

# Define a classe NodeManager, que gerencia uma lista de objetos Node
class NodeManager:
    # Define o atributo 'nodes' como uma lista de objetos Node
    nodes: List[Node]

    # Construtor da classe que recebe uma lista de objetos Node
    def __init__(self, nodes: List[Node]):
        # Verifica se o parâmetro recebido é uma lista e se todos os itens são instâncias da classe Node
        if not isinstance(nodes, list) or not all(isinstance(node, Node) for node in nodes):
            # Se a condição não for atendida, levanta uma exceção ValueError
            raise ValueError("O parâmetro 'nodes' deve ser uma lista de objetos Node.")
        # Armazena os nós na lista interna _nodes, garantindo que a lista original não seja mutada
        self._nodes = list(nodes)

    # Propriedade para acessar os nós armazenados
    @property
    def nodes(self):
        # Retorna a lista de nós armazenada
        return self._nodes

    # Método especial __len__ para permitir o uso de len() em uma instância de NodeManager
    def __len__(self):
        # Retorna o número de nós armazenados
        return len(self.nodes)

    # Método especial __getitem__ para permitir o acesso aos nós por índice, como se fosse uma lista
    def __getitem__(self, index: int):
        # Retorna o nó no índice fornecido
        return self.nodes[index]

    # Método remove para remover um nó específico, sem afetar seus descendentes
    def remove(self, node: Node):
        # Itera sobre a lista de nós para encontrar o nó a ser removido
        for n in self.nodes:
            # Compara o id e parent do nó para garantir que estamos removendo o nó correto
            if n.id == node.id and n.parent == node.parent:
                # Remove o nó da lista
                self.nodes.remove(n)
                return
        # Se o nó não for encontrado, levanta uma exceção ValueError
        raise ValueError("O nó a ser removido não existe.")

    # Método remove_cascade para remover um nó e todos os seus descendentes
    def remove_cascade(self, node: Node):
        # Verifica se o nó existe na lista de nós
        if node not in self.nodes:
            # Se o nó não existir, levanta uma exceção ValueError
            raise ValueError("O nó a ser removido não existe.")

        # Lista para armazenar todos os nós que serão removidos
        nodes_to_remove = []

        # Função recursiva para encontrar todos os descendentes do nó
        def collect_descendants(parent_node):
            # Itera sobre todos os nós para encontrar aqueles que são filhos do nó atual
            for n in self.nodes:
                if n.parent == parent_node.id:
                    # Adiciona os filhos encontrados à lista de nós a serem removidos
                    nodes_to_remove.append(n)
                    # Chama a função recursivamente para coletar os filhos dos filhos
                    collect_descendants(n)

        # Coleta todos os descendentes do nó
        collect_descendants(node)

        # Remove todos os descendentes da lista de nós
        for descendant in nodes_to_remove:
            self.nodes.remove(descendant)

        # Remove o nó original (o nó que foi passado como argumento)
        self.nodes.remove(node)
