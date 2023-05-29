print('Bem-vindo a lanchonete da Raiane Isabela Bryk')
print('-----------------Cardápio-----------------')
print('| Código |       Descrição       | Valor |')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |         X-Egg         | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |        X-Tudo         | 17,00 |')
print('|   200  |   Refrigerante Lata   |  5,00 |')
print('|   201  |       Chá Gelado      |  4,00 |')
print('------------------------------------------')
valor = 0
while True:
    # Validação caso o código digitado seja inválido
    codigo = input('Entre com o código desejado: ')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Opção Inválida!')
        continue # se o usuário digitar algo inválido volta para o começo do while

    # validação do código escolhido e soma dos valores
    if codigo == '100':
        print('Você pediu um Cachorro Quente no valor de R$ 9,00')
        valor += 9
    elif codigo == '101':
        print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00')
        valor += 11
    elif codigo == '102':
        print('Você pediu um X-Egg no valor de R$ 12,00')
        valor += 12
    elif codigo == '103':
        print('Você pediu um X-Salada no valor de R$ 12,00')
        valor += 12
    elif codigo == '104':
        print('Você pediu um X-Bacon no valor de R$ 14,00')
        valor += 14
    elif codigo == '105':
        print('Você pediu um X-Tudo no valor de R$ 17,00')
        valor += 17
    elif codigo == '200':
        print('Você pediu um Refrigerante Lata no valor de R$ 5,00')
        valor += 5
    elif codigo == '201':
        print('Você pediu um Chá Gelado no valor de R$ 4,00')
        valor += 4
    else:
        print('Opção Inválida!')

    # validação de adicionar mais algum pedido
    adicional = input('Deseja pedir mais alguma coisa? \n 1- Sim \n 0- Não \n')
    if adicional == '1':
        continue # se o usuário digitar 1 volta para o começo do while
    else:
        print('O total a ser pago é: R$ {:.2f}'.format(valor))
        break


