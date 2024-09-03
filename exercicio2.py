#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
#será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#escreva um programa na linguagem que desejar onde, informado um número, ele calcule
#a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou
#não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência
# ou pode ser previamente definido no código.


def validaFibonacci(num):
    a = 0
    b = 1
    
    if num == 0 or num == 1:
        print(f"o numero: {num} pertence à sequência!")

    while b < num:
        temp = a + b
        a = b
        b = temp
    if b == num:
        print(f"o numero: {num} pertence à sequência!")
    else:
        print(f"o numero: {num} não pertence à sequência!")
        
numero = int(input("digite um número: "))
print(validaFibonacci(numero))