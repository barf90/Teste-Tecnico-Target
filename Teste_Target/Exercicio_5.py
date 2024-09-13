# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

frase = str(input("Digite a string desejada: ")) # input da string desejada

tamanho_frase = len(frase) # pegando o tamanho da frase

while tamanho_frase > 0: # loop para inverter a string
    print(frase[tamanho_frase-1], end='') # print da string invertida
    tamanho_frase -= 1