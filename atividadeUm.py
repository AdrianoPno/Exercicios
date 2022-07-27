print ("Bem vindo a loja do Adriano Dias Alves da Silva")

while True:
    qtdPecas = int(input('Digite a quantidade de produto(os): '))
    valorProduto = float(input('Digite o valor do produto: '))

    total = qtdPecas * valorProduto # valor a ser pago pelo cliente
    global desconto         # valor a ser pago pelo cliente com desconto

    if qtdPecas <= 9:
       desconto = total # print ('teste não teve desconto')
    elif qtdPecas >= 10 and qtdPecas <= 99:
        desconto = total - (total * 5/100) # print('teste 5%')
    elif qtdPecas >= 100 and qtdPecas <= 999:
        desconto = total - (total * 10/100) # print('teste 10%')
    else:
        desconto = total - (total * 15/100) # print('teste 15%')

    print('O valor sem desconto foi: R$ {:.2f}' .format(total))
    print('O valor com desconto foi: R$ {:.2f}' .format(desconto))

    break
