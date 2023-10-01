# Tipo de Dado Abstrato Set (Conjunto):
O Tipo de Dado Abstrato Set (conjunto) é uma estrutura de dados que suporta as operações de inserção, remoção e consulta de elementos, além das operações de união, interseção e diferença entre conjuntos.
Neste trabalho, o objetivo é implementar as operações do Tipo de Dado Abstrato Set, utilizando uma estrutura de dados que permita sua implementação de forma eficiente.

## Escolha da Estrutura de Dados:
Para a implementação deste Tipo de Dado Abstrato Set, optou-se por utilizar uma lista (self.dados). A escolha dessa estrutura foi baseada na premissa de simplicidade e clareza. Embora não seja a estrutura de dados mais eficiente para todas as operações, a lista proporciona facilidade de compreensão e permite a implementação direta das operações essenciais de um conjunto.

## Complexidade de Tempo Esperada:
* **Inserção (inserir):** O(n) no pior caso (quando o elemento já existe no conjunto).
* **Remoção (remover):** O(n) no pior caso (quando o elemento a ser removido está no final da lista).
* **Consulta (contém):** O(n) no pior caso (quando o elemento não está no conjunto).
* **União (união):** O(m * n) no pior caso (quando há muitos elementos em comum entre os conjuntos, onde "m" e "n" são os tamanhos dos conjuntos).
* **Interseção (interseção):** O(m * n) no pior caso (pelo mesmo motivo da operação de união).
* **Diferença (diferença):** O(m * n) no pior caso (também pelo mesmo motivo da operação de união).

## Complexidade de Espaço Esperada:
O(n), onde "n" é o número de elementos no conjunto.

## Conclusão:
A escolha da estrutura de dados depende das prioridades, requisitos de desempenho e complexidade do problema específico enfrentado.
Embora a implementação com lista seja simples e fácil de entender, não é a mais eficiente para operações como união, interseção e diferença de conjuntos, que podem ser otimizadas usando estruturas de dados mais adequadas, como tabelas de hash ou conjuntos embutidos (por exemplo, a classe 'set' em Python).
No entanto, para conjuntos pequenos ou aplicações simples, a implementação com lista pode ser suficiente.
