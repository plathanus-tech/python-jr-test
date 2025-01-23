# Definindo a classe Node
class Node:
    # Atributos id e parent da classe Node, ambos do tipo inteiro
    id: int
    parent: int

    # Construtor da classe Node, que recebe dois parâmetros: id e parent
    def __init__(self, id: int, parent: int):
        # Verifica se os parâmetros id e parent são inteiros
        if not isinstance(id, int) or not isinstance(parent, int):
            # Se não forem inteiros, levanta uma exceção ValueError com uma mensagem explicativa
            raise ValueError("Os Valores de 'id' e 'parent' devem ser inteiros.")
        
        # Verifica se o valor de parent não é maior que o de id
        if parent > id:
            # Se parent for maior que id, levanta uma exceção ValueError
            raise ValueError("O valor de 'parent' não pode ser maior que o 'id'.")
        
        # Verifica se o valor de parent não é igual a id
        if id == parent:
            # Se parent for igual a id, levanta uma exceção ValueError
            raise ValueError("O valor de 'parent' não pode ser igual ao 'id'.")
        
        # Se todas as condições forem atendidas, os valores de id e parent são atribuídos aos atributos da instância
        self.id = id
        self.parent = parent
    
    # Método especial __repr__ para retornar uma representação da instância de Node de forma mais legível
    def __repr__(self):
        # Retorna uma string formatada com o id e parent, que é útil para depuração
        return f"Node({self.id}, {self.parent})"
