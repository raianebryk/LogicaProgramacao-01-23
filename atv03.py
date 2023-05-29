print('Bem-vindo a Companhia de Logistica Raiane Isabela Bryk S.A.')
def dimensoesObjeto():
    while True:
        try:
            comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            largura = float(input('Digite a largura do objeto (em cm): '))
            altura = float(input('Digite a altura do objeto (em cm): '))
            volume = comprimento * largura * altura
            # validação do volume do objeto
            if volume < 1000:
                print('O volume do objeto é (em cm³): {}'.format(volume))
                return 10
            elif volume >= 1000 and volume < 10000:
                print('O volume do objeto é (em cm³): {}'.format(volume))
                return 20
            elif volume >= 10000 and volume < 30000:
                print('O volume do objeto é (em cm³): {}'.format(volume))
                return 30
            elif volume >= 30000 and volume < 100000:
                print('O volume do objeto é (em cm³): {}'.format(volume))
                return 50
            else:
                print('O volume do objeto é (em cm³): {}'.format(volume))
                print('Não aceitamos objetos com dimensões tão grandes \n' +
                      'Entre com as dimensões desejadas novamente')
        # caso o usuário não digite um valor numérico
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico \n' +
                  'Por favor entre com as dimensões desejadas novamente')

def pesoObjeto():
    while True:
        try:
            pesoKg = float(input('Digite o peso do objeto (em kg): '))
            # validação do peso do objeto
            if pesoKg <= 0.1:
                return 1
            elif pesoKg >= 0.1 and pesoKg < 1:
                return 1.5
            elif pesoKg >= 1 and pesoKg < 10:
                return 2
            elif pesoKg >= 10 and pesoKg < 30:
                return 3
            else:
                print('Não aceitamos objetos tão pesados \n' +
                      'Entre com o peso desejado novamente')
        # caso o usuário não digite um valor numérico
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico \n' +
                  'Por favor entre com o peso desejado novamente')

def rotaObjeto():
    while True:
        rotaObj = input('Selecione a rota: \n' +
                        'RS - De Rio de Janeiro até São Paulo \n' +
                        'SR - De São Paulo até Rio de Janeiro \n' +
                        'BS - De Brasília até São Paulo \n' +
                        'SB - De São Paulo até Brasília \n' +
                        'BR - De Brasília até Rio de Janeiro \n' +
                        'RB - De Rio de Janeiro até Brasília \n' +
                        '>> ')
        rotaObj = rotaObj.upper() # caso o usuário digite em minúsculo
        # validção da rota do objeto
        if rotaObj == 'RS' or rotaObj == 'SR':
            return 1
        elif rotaObj == 'BS' or rotaObj == 'SB':
            return 1.2
        elif rotaObj == 'BR' or rotaObj == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe \n' +
                  'Por favor entre com a rota desejada novamente')

dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print('Total a pagar(R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, dimensoes, peso, rota))