# Função para carregar as definições do autômato a partir de um arquivo
def carregar_automato(projeto):
    transicoes = {}  # Dicionário para armazenar as transições entre os estados
    with open(projeto, 'r') as arquivo:
        estado_inicial = arquivo.readline().strip()  # Lê o estado inicial e remove espaços extras
        alfabeto = set(arquivo.readline().split())  # Lê os símbolos do alfabeto e os coloca em um conjunto
        estados = set(arquivo.readline().split())  # Lê os estados e os coloca em um conjunto
        estados_finais = set(arquivo.readline().split())  # Lê os estados finais e os coloca em um conjunto

        for linha in arquivo:
            partes = linha.split()  # Divide a linha em partes (estado_origem, simbolo, estado_destino)
            estado_origem, simbolo, estado_destino = partes[0], partes[2], partes[1]
            if estado_origem not in transicoes:
                transicoes[estado_origem] = {}  # Cria um dicionário para armazenar as transições do estado_origem
            transicoes[estado_origem][simbolo] = estado_destino  # Define a transição entre estado_origem e estado_destino

    # Retorna as informações carregadas do arquivo
    return estado_inicial, alfabeto, estados, estados_finais, transicoes

# Função para verificar se uma palavra é aceita pelo autômato
def e_aceito(automato, palavra):
    estados_atuais = {automato[0]}  # Começa com o estado inicial
    proximos_estados = set()
    for simbolo in palavra:
        if simbolo not in automato[1]:  # Se o símbolo não estiver no alfabeto, a palavra é rejeitada
            return False
        for estado in estados_atuais:
            if estado in automato[4] and simbolo in automato[4][estado]:
                proximos_estados.add(automato[4][estado][simbolo])  # Adiciona os próximos estados possíveis
        estados_atuais, proximos_estados = proximos_estados, set()  # Atualiza os estados atuais
    # Verifica se algum estado atual é um estado final
    return any(estado in automato[3] for estado in estados_atuais)

# Função principal
def main():
    automato = carregar_automato("projeto.txt")  # Carrega as definições do autômato a partir do arquivo

    palavra = input("Digite a palavra: ")  # Solicita a palavra ao usuário
    if e_aceito(automato, palavra):  # Verifica se a palavra é aceita pelo autômato
        print("Aceita")
    else:
        print("Rejeita")

# Verifica se o código está sendo executado como programa principal
if __name__ == "__main__":
    main()  # Chama a função principal
