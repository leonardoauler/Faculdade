class AutomatoFinitoDeterministico:
    def __init__(self):
        # Define os estados possíveis do autômato.
        self.estados = {'q0', 'q1', 'q2', 'q3'}
        
        # Define os símbolos do alfabeto.
        self.alfabeto = {'a', 'b'}
        
        # Define as transições entre os estados baseado nos símbolos do alfabeto.
        self.transicoes = {
            'q0': {'a': 'q1'},  # Do estado q0 para q1 ao ler 'a'.
            'q1': {'a': 'q1', 'b': 'q2'},  # Do estado q1 para q1 ao ler 'a', ou para q2 ao ler 'b'.
            'q2': {'a': 'q3', 'b': 'q1'},  # Do estado q2 para q3 ao ler 'a', ou para q1 ao ler 'b'.
            'q3': {}  # Estado q3 não tem transições definidas, o autômato termina aqui.
        }
        
        # Define o estado inicial do autômato.
        self.estado_inicial = 'q0'
        
        # Define os estados finais do autômato.
        self.estados_finais = {'q1', 'q3'}

    def esta_aceita(self, palavra):
        estado_atual = self.estado_inicial
        
        # Percorre os símbolos da palavra para determinar a sequência de estados.
        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False
            if estado_atual not in self.transicoes or simbolo not in self.transicoes[estado_atual]:
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        
        # Verifica se o estado final é um estado aceito.
        return estado_atual in self.estados_finais


def main():
    automato = AutomatoFinitoDeterministico()

    # Solicita ao usuário que insira uma palavra.
    palavra = input("Digite a palavra: ")
    
    # Verifica se a palavra é aceita ou rejeitada pelo autômato.
    if automato.esta_aceita(palavra):
        print("Aceita")
    else:
        print("Rejeita")


if __name__ == "__main__":
    main()