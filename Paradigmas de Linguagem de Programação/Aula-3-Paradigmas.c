#include <stdio.h>

int main() {
    int num, maior, menor, soma, cont;
    double media;

    printf("Digite os valores inteiros (0 para encerrar):\n");

    maior = menor = soma = cont = 0;

    do {
        scanf("%d", &num);

        if (num != 0) {
            if (cont == 0 || num > maior) {
                maior = num;
            }

            if (cont == 0 || num < menor) {
                menor = num;
            }

            soma += num;
            cont++;
        }
    } while (num != 0);

    if (cont > 0) {
        media = (double) soma / cont;

        printf("Maior número lido: %d\n", maior);
        printf("Menor número lido: %d\n", menor);
        printf("Média dos números inseridos: %.2f\n", media);
    } else {
        printf("Nenhum número foi inserido.\n");
    }

    return 0;
}