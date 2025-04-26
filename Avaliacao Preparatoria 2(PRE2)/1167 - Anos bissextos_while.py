def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

inicio = int(input())
fim = int(input())
qtd_bissextos = 0

ano = inicio

while ano <= fim:
    if bissexto(ano):
        print(ano)
        qtd_bissextos +=1

    ano +=1
    
print(f'bissextos: {qtd_bissextos}')            

