'''
Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

Obs.: Seu programa deverá usar, de modo coerente, um laço de repetição. Não serão aceitas soluções que não obedecerem esta regra.

Entrada

Um número natural N (0 <= N <= 10).

Saída

Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos.
'''
n = int(input())

for i in range (1, 11):
    print(f'{n} x {i} = {n*i}')
