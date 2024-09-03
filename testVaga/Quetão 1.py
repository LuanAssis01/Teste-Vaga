import math

def eh_quadrado_perfeito(x):
    s = int(math.sqrt(x))
    return s * s == x

def pertence_a_fibonacci(n):

    return eh_quadrado_perfeito(5*n*n + 4) or eh_quadrado_perfeito(5*n*n - 4)

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n-1)
        prox_num = sequence[-1] + sequence[-2]
        sequence.append(prox_num)
        return sequence
x = int(input("Digite o valor de x: "))

if pertence_a_fibonacci(x):
    print(f"O número {x} pertence à sequência de Fibonacci.")
else:
    print(f"O número {x} NÃO pertence à sequência de Fibonacci.")
