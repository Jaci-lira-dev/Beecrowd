'''
Você sabe o que são anos bissextos? Resumidamente, em anos bissextos o mês de fevereiro é mais extenso, contendo 29 dias, ao invés de apenas 28. O cálculo para descobrir se um ano é bissexto também é bastante simples, pois um ano é bissexto se é divisível por 4 e não por 100, ou se é divisível por 400.

Claudia adora anos bissextos, porque ela nasceu em um! Mais precisamente, Claudia nasceu no dia 29 de fevereiro, por isso sente que seu aniversário só ocorre "de verdade" nos anos que são bissextos, afinal pode projetar a festa sem ter que explicar aos amigos se comemorará no dia 28 de fevereiro ou no dia 01 de março.

Você foi convidado para a comemoração de Claudia, mas para isso ela pediu um presente especial, solicitou que você construa um programa que a ajude a ficar menos ansiosa para saber quais são os anos em que ela poderá realizar festas na data correta. Para isso, seu programa deverá receber um ano INÍCIO e um ano FIM e exibir todos os anos bissextos do intervalo fechado [ INÍCIO..FIM ]. Ao final, o programa também deve exibir a quantidade de anos bissextos do intervalo.

Entrada

Dois números naturais, um em cada linha, que representam o ano INÍCIO e o ano FIM do intervalo considerado. Adote que (0 <= INÍCIO <= FIM <= 9999) sempre será verdade.

Saída

Todos os anos bissextos do intervalo fechado [ INÍCIO..FIM ], um por linha. Ao final, o programa também deve exibir a quantidade de anos bissextos do intervalo [ INÍCIO..FIM ], conforme os exemplos.'''

def bissexto(ano):
    return (ano % 4 ==0 and ano % 100 != 0) or ano % 400 == 0

inicio = int(input())
fim = int(input())
qtd_bissextos = 0

for ano in range(inicio, fim+1):
    if bissexto(ano):
        print(ano)
        qtd_bissextos += 1

print(f'bissextos: {qtd_bissextos}')