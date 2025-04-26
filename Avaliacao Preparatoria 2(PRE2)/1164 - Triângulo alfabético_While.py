'''
Como dito por um importante personagem de um igualmente memorável filme: "palavras são, na minha nada humilde opinião, nossa inesgotável fonte de magia [...]". Evidentemente, para formar palavras é necessário que exista um alfabeto como, por exemplo, nosso alfabeto latino.

O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres diferentes, se desconsiderarmos as acentuações e as diferenças entre letras maiúsculas e minúsculas.

Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. Em um dos desenhos, Harry escreve na primeira linha e primeira coluna de uma folha quadriculada o primeiro caractere do alfabeto. Na segunda linha escreve duas vezes o segundo caractere, ocupando as duas primeiras colunas. Na terceira linha escreve três vezes o terceiro caractere, ocupando as três primeiras colunas e assim por diante. Harry percebeu que dessa forma consegue formar um triângulo alfabético, semelhante ao visto na Figura 1, onde a primeira linha contém apenas um 'A' e a sétima contém sete 'G'.

Figura 1: Triângulo Alfabético com sete linhas.



Como Harry precisa estudar para realizar uma prova de programação (que para ele também é uma forma de magia!), pediu sua ajuda para automatizar os desenhos dos "triângulos alfabéticos", criando um programa que receba como entrada um número inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a mesma estratégia descrita no texto. Note que o maior triângulo possível é aquele formado por vinte e seis linhas, onde na primeira linha há apenas um caractere 'A' e na última há somente vinte e seis caracteres 'Z'.

Entrada
Um número inteiro N (1 <= N <= 26).

Saída
Um triângulo alfabético com exatas N linhas e com a mesma estratégia de construção mencionada no texto. Note que as letras são sempre maiúsculas. '''

n = int(input())

letra = 'A'
linha = 1

while linha < n+1:
    print(letra * linha)
    letra = chr(ord(letra) + 1)
    linha +=1
        