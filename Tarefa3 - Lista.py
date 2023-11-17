#Crie um programa que utilize a lista L = [5, 7, 2, 9, 4, 1, 3] e exiba as seguintes informações:
# Quantidade de elementos presentes na lista.
#• O maior valor presente na lista.
#• O menor valor presente na lista.
#• A soma de todos os elementos da lista.
#• A lista em ordem crescente.
#• A lista em ordem decrescente.

# Como criar listas 
# Sintaxe nome_da_lista = ['elementos da lista' - separados por virgula]

lista = []
mai = 0
men = 0 
for c in range (0, 7):
    lista.append(int(input(f'Digite um valor para a posição {c}:  ')))
    if c== 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('*'*50)
print (f'Você digitou os valores {lista}')
print (f'O maior valor digitado foi: {mai}')
print (f'O menor valor digitado foi: {men}')
print ('*'*50)
soma = sum(lista)
print('A soma da lista é ', soma)

lista.sort()
print('A lista em ordem crescente é', lista)
print('*'*50)
lista = sorted(lista, reverse=True)
print('A lista em ordem decrescente é', lista)
