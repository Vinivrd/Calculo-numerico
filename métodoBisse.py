import math
def bissecao(funcao, a, b, tol=1e-12, max_iter=1000):
    """
    Método da bisseção para encontrar a raiz de uma função.

    :param funcao: A função para a qual queremos encontrar a raiz.
    :param a: O limite inferior do intervalo inicial.
    :param b: O limite superior do intervalo inicial.
    :param tol: A tolerância para a convergência.
    :param max_iter: O número máximo de iterações permitidas.
    :return: A aproximação da raiz da função.
    """
    if funcao(a) * funcao(b) >= 0:
        raise ValueError("A função deve mudar de sinal em [a, b].")

    iteracao = 0
    while (b - a) / 2 > tol and iteracao < max_iter:
        c = (a + b) / 2
        if funcao(c) == 0:
            return c
        elif funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c
        iteracao += 1

    return (a + b) / 2, iteracao

# Exemplo de uso:
def funcao_exemplo(x):
    return x**2 - math.sin(x)

raiz,itera = bissecao(funcao_exemplo, 0.5, 2)
print("A raiz da função é aproximadamente:", raiz)
print("Número de iterações:", itera)