import time
limpa = '\33[m'
amarelo = '\33[33m'
pretoebranco = '\33[30;7m'
ciano = '\33[36m'
branco = '\33[30m'
verm = '\33[31m'
op = 'asdasdasd'
n1 = int(input('Digite o seu primeiro valor: '))
n2 = int(input('Digite o seu segundo valor: '))
while op != 5:
    print('@@@@@@@@@@@@@@@@@@@@@@@@\n [ 1 ] Somar\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Outros numeros\n [ 5 ] Fechar programa\n@@@@@@@@@@@@@@@@@@@@@@@@')
    op = int(input('Sua operacao: '))
    if op == 1:
        print('{}A soma entre {} e {} eh {}{}{}'.format(amarelo,n1,n2,ciano,n1 + n2,limpa))
    elif op == 2:
        print('{}A multiplicacao entre {} e {} eh {}{}{} '.format(amarelo,n1,n2,ciano,n1 * n2,limpa))
    elif op == 3:
        if n1 > n2:
            print('{}Entre {} e {} o maior eh {}{}{}'.format(amarelo,n1,n2,ciano,n1,limpa))
        elif n2 > n1:
            print('{}Entre {} e {} o maior eh {}{}{}'.format(amarelo,n1,n2,ciano,n2,limpa))
        else:
            print('{}Os dois numeros sao iguais{}'.format(amarelo,limpa))
    elif op == 4:
        n1 = int(input('{}Digite o seu primeiro novo valor: '.format(amarelo)))
        n2 = int(input('Digite o seu segundo novo valor: {}'.format(limpa)))
    elif op == 5:
        op = 5
    else:
        print('{}Digite uma das opcoes abaixo{}'.format(verm,limpa))
print('Finalizando o programa...')
time.sleep(2)