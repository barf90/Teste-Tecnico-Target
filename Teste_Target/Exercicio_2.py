# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci(n): # Função recursiva para calcular a sequencia de Fibonacci
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main(): # Função main, onde vai o código principal
    numero = int(input("Digite o número desejado: ")) # input do número desejado 

    i = 0 # Limitador da sequencia até encontrar um número maior ou igual ao número informado

    while True:
        f = fibonacci(i)

        if f == numero:
            print("o número informado pertence a sequência")
            break

        elif f > numero:
            print("o número informado não pertence a sequência")
            break

        i += 1

if __name__ == '__main__': # Inicializando a main
    main()