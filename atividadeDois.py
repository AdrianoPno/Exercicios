#CABEÇALHO
titulo = 'BEM VINDO A LANCHONETE DO Adriano Dias Alves da Silva'
menu = 'C A R D A P I O'
coluna1 = 'C O D I G O'
coluna2 = 'D E S C R I C A O'
coluna3 = 'V A L O R'

#codigo #descrição #valor
#contem caracteristicas de cada produto
class Produto:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
    pass
produto1 = Produto('100', 'Cachorro Quente', '9.00')
produto2 = Produto('101', 'Cachorro Quente Duplo', '11.00')
produto3 = Produto('102', 'X - Egg', '12.00')
produto4 = Produto('103', 'X - Salada', '13.00')
produto5 = Produto('104', 'X - Bacon', '14.00')
produto6 = Produto('105', 'X - Tudo', '17.00')
produto7 = Produto('200', 'Refrigerante Lata', '5.00')
produto8 = Produto('201', 'Cha Gelado', '4.00')


print(f" {titulo:^75} ")
print(f" {menu:^75} ")
print(f"| {coluna1:^23} | {coluna2:^23} | {coluna2:^23} |")
print(f"| {produto1.codigo:^23} | {produto1.descricao:^23} | {produto1.valor:^23} |")
print(f"| {produto2.codigo:^23} | {produto2.descricao:^23} | {produto2.valor:^23} |")
print(f"| {produto3.codigo:^23} | {produto3.descricao:^23} | {produto3.valor:^23} |")
print(f"| {produto4.codigo:^23} | {produto4.descricao:^23} | {produto4.valor:^23} |")
print(f"| {produto5.codigo:^23} | {produto5.descricao:^23} | {produto5.valor:^23} |")
print(f"| {produto6.codigo:^23} | {produto6.descricao:^23} | {produto6.valor:^23} |")
print(f"| {produto7.codigo:^23} | {produto7.descricao:^23} | {produto7.valor:^23} |")
print(f"| {produto8.codigo:^23} | {produto8.descricao:^23} | {produto8.valor:^23} |")



total = 0 #Variavel Acumuladora, guarda a soma

while True:

    pedido = int(input('Informe o codigo: '))
    if(pedido == 777):
        break

    if pedido == 100:
        print("Você pediu um Cachorro quente no valor de R$ 9.00")
        total = total + 9.00
    elif pedido == 101:
        print("Você pediu um Cachorro quente Duplo no valor de R$ 11.00")
        total = total + 11.00
    elif pedido == 102:
        print("Você pediu um X - Egg no valor de R$ 12.00")
        total = total + 12.00
    elif pedido == 103:
        print("Você pediu um X - Salada no valor de R$ 13.00")
        total = total + 13.00
    elif pedido == 104:
        print("Você pediu um X - Bacon no valor de R$ 14.00")
        total = total + 14.00
    elif pedido == 105:
        print("Você pediu um X - Tudo no valor de R$ 17.00")
        total = total + 17.00
    elif pedido == 200:
        print("Você pediu um Refrigerante Lata no valor de R$ 5.00")
        total = total + 5.00
    elif pedido == 201:
         print("Você pediu um Cha Gelado no valor de R$ 4.00")
         total = total + 4.00
    else:
        print('Codigo invalido')
        continue

    continuar = input('deseja comprar outro item:\n'
                      '1 - SIM\n'
                      '2 - NÃO \n'
                      '>> ')

    if continuar == '1':
        continue
    else:
        continuar == '2'
        print('O valor final da sua compra é: R$ {:.2f}'.format(total))
        print('Obrigado, volte sempre!')

        break
