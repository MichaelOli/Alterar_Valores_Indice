# lista
nomes = ['Michael', 'Micaely', 'Fabio', 'César', 'Alexander','Tatiane']

#usuario informa o índice que deseja alterar
indice = int(input('Informe o indice que deseja alterar: '))
indice -=1
#usuario informa o novo nome
nomes[indice] = input('Informe o novo nome: ')

#imprime a lista inteira
for nome in nomes: 
    print(nome)