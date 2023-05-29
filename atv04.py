lista_peca = []
codigo_peca = 0
def cadastrarPeca(codigo):
    print('Você Selecionou a Opção Cadastrar Peça')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Por favor entre com o NOME da peça: ')
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor entre com o VALOR da peça: '))
    dicionario_valor = {'codigo': codigo,
                        'nome': nome,
                        'fabricante': fabricante,
                        'valor': valor}
    lista_peca.append(dicionario_valor.copy()) # copia para a lista

def consultarPeca():
    print('Você Selecionou a Opção Consultar Peça')
    while True:
        opcao_consultar = input('Escolha a opção desejada: \n' +
                                '1 - Consultar Todas as Peças \n' +
                                '2 - Consultar Peças po Código \n' +
                                '3 - Consultar Peças por Fabricante \n' +
                                '4 - Retornar \n' +
                                '>> ')
        if opcao_consultar == '1':
            for peca in lista_peca: # peça varre toda a lista de peças
                print('--------------------')
                for key,value in peca.items(): # varre todos os conjuntos chave e o valor do dicionário
                    print('{}: {}'.format(key,value))
                print('--------------------')
        elif opcao_consultar == '2':
            valor_desejado = int(input('Digite o CÓDIGO da peça: '))
            for peca in lista_peca:
               if peca['codigo'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
                print('--------------------')
                for key,value in peca.items(): # varre todos os conjuntos chave e o valor do dicionário
                    print('{}: {}'.format(key,value))
            print('--------------------')
        elif opcao_consultar == '3':
            valor_desejado = input('Digite o FABRICANTE da Peça: ')
            for peca in lista_peca:
                if peca['fabricante'] == valor_desejado: # o valor do campo fabricante desse dicionário é igual o valor desejado
                    print('--------------------')
                    for key,value in peca.items(): # varre todos os conjuntos chave e o valor do dicionário
                        print('{}: {}'.format(key,value))
                print('--------------------')
        elif opcao_consultar == '4':
            return # sai da função opcao_consultar e volta para o Main
        else:
            print('Opção Inválida. Tente Novamente!')

def removerPeca():
    print('Você Selecionou a Opção Remover Peça')
    valor_desejado = int(input('Digite o código da peça a ser removida: '))
    for peca in lista_peca:
        if peca['codigo'] == valor_desejado: # o valor do campo código desse dicionário é igual o valor desejado
            lista_peca.remove(peca) # remove da lista
            print('Peça Removida')


print('Bem vindo ao Controle de Estoque da Bicicletaria da Raiane Isabela Bryk')
while True:
    opcao_principal = input('Escolha a opção desejada: \n' +
                            '1 - Cadastrar Peças \n' +
                            '2 - Consultar Peças \n' +
                            '3 - Remover Peças \n' +
                            '4 - Sair \n' +
                            '>> ')
    # validação de escolha
    if opcao_principal == '1':
        codigo_peca += 1
        cadastrarPeca(codigo_peca)
    elif opcao_principal == '2':
        consultarPeca()
    elif opcao_principal == '3':
        removerPeca()
    elif opcao_principal == '4':
        break # encera o laço principal e o programa acaba
    else:
        print('Opção Inválida. Tente Novamente!')
        continue # volta para o início do laço