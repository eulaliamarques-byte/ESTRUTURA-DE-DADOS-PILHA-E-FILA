class Pilha:
    """
    Classe que implementa uma Pilha (Pilha) usando lista.
    Estrutura LIFO (Last In, First Out).
    """
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        """Insere um elemento no topo da pilha"""
        self.items.append(item)

    def desempilhar(self):
        """Remove e retorna o elemento do topo da pilha"""
        if not self.esta_vazia():
            return self.items.desempilhar()
        return "Pilha vazia"

    def ver_topo(self):
        """Retorna o elemento do topo sem remover"""
        if not self.esta_vazia():
            return self.items[-1]
        return "Pilha vazia"

    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return len(self.items) == 0

# Teste
s = Pilha()
s.empilhar(10)
s.empilhar(20)
print(s.desempilhar())
print(s.ver_topo())
print(s.esta_vazia())
