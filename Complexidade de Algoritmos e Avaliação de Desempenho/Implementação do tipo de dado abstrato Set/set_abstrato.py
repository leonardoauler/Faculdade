class Set:
    def __init__(self):
        self.dados = []

    def insert(self, valor):
        if valor not in self.dados:
            self.dados.append(valor)

    def remove(self, valor):
        if valor in self.dados:
            self.dados.remove(valor)

    def contem(self, valor):
        return valor in self.dados

    def uniao(self, outro_set):
        novo_set = Set()
        novo_set.dados = self.dados.copy()
        for item in outro_set.dados:
            if item not in novo_set.dados:
                novo_set.dados.append(item)
        return novo_set

    def intersection(self, outro_set):
        novo_set = Set()
        for item in self.dados:
            if item in outro_set.dados:
                novo_set.insert(item)
        return novo_set

    def difference(self, outro_set):
        novo_set = Set()
        for item in self.dados:
            if item not in outro_set.dados:
                novo_set.insert(item)
        return novo_set

    def __str__(self):
        return "{" + ", ".join(map(str, self.dados)) + "}"


# Exemplo de uso:
nosso_set = Set()
nosso_set.insert(1)
nosso_set.insert(2)
nosso_set.insert(3)

print("Set nosso_set:", nosso_set)  # Saída: Set nosso_set: {1, 2, 3}

nosso_set.remove(2)
print("nosso_set apos remover 2:", nosso_set)  # Saída: nosso_set após remover 2: {1, 3}

print("O conjunto nosso_set contem 3?", nosso_set.contem(3))  # Saída: True
print("O conjunto nosso_set contem 2?", nosso_set.contem(2))  # Saída: False

outro_set = Set()
outro_set.insert(3)
outro_set.insert(4)
outro_set.insert(5)

uniao_set = nosso_set.uniao(outro_set)
print("Uniao de nosso_set e outro_set:", uniao_set)  # Saida: Uniao de nosso_set e outro_set: {1, 3, 4, 5}

intersection_set = nosso_set.intersection(outro_set)
print("Intersecao de nosso_set e outro_set:", intersection_set)  # Saida: Intersecao de nosso_set e outro_set: {3}

difference_set = nosso_set.difference(outro_set)
print("Diferenca entre nosso_set e outro_set:", difference_set)  # Saida: Diferenca entre nosso_set e outro_set: {1}
