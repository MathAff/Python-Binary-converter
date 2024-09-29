import time as t
import platform
import os

system = str(platform.system())
csC = ""
if system == "Windows":
    csC = "cls"
elif system == "Linux":
    csC = "clear"

os.system(csC)

def d_b ():
    n0 = str(input(f'Digite um número decimal para ser convertido em binário: '))
    os.system(csC)
    n1 = int(n0)
    n2 = n0
    rest_str = ''
    rest = ''
    while n1 > 1:
        rest = n1 % 2
        n1 = n1 // 2
        rest_str = str(rest) + rest_str
        n0 = str(n1)
    rest_str = n0 + rest_str
    print (f'O valor de {n2} em binário é: ')
    print (rest_str)

def b_d ():
    binary = list(str(input(f"Digite o número em binário para ser convertido em decimal: ")))
    os.system(csC)
    binary.reverse()
    for i in range (len(binary)):
        binary [i] = int(binary [i]) * 2 ** i
    print(f'O valor do número binário em decimal é igual a: ')
    print (sum(binary))

print (30 * '=')
print (f'CONVERSOR DE BINÁRIO')
print (30 * '=')
print (f'Este programa converte decimal para binário ou binário para decimal')
input (f'Precione ENTER para comecar')
i = 's'
while i == 's':
    os.system(csC)
    c = str(input("Converter decimal (D) ou binário (B)? ")).lower()
    os.system(csC)
    if c == 'd':
        d_b()
    elif c == 'b':
        b_d()
    else:
        print(f'ERRO, OPÇÃO NÃO EXISTENTE')
    t.sleep(2)
    i = str(input('Continuar?(S/N) ')).lower()
print ('Obrigado, volte sempre :)')
t.sleep(2)
os.system(csC)