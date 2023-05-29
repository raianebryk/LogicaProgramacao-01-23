print('Bem Vindo a loja da Raiane Isabela Bryk')
valor_produto = float(input('Entre com o valor do produto: '))
qtd = int(input('Entre com o valor da quantidade: '))
desconto = 0
# O desconto somente será concedido com a quantidade acima de 9 itens
# Sendo 5% de desconto de 10 itens até 99, 10% de desconto de 100 itens até 999 e acima disso 15% de desconto
if (qtd < 10):
    desconto = 0.00
elif (10 <= qtd < 100):
    desconto = 0.05
elif (100 <= qtd < 1000):
    desconto = 0.10
else:
    desconto = 0.15
valor_sem_desconto = valor_produto * qtd
print('O valor sem desconto foi: {}'.format(valor_sem_desconto))
valor_com_desconto = valor_sem_desconto - valor_sem_desconto * desconto
print('O valor com desconto foi: {:.2f} (desconto {}%)'. format(valor_com_desconto, int(desconto*100)))