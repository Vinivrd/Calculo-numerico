import numpy as np

def calK(x):

    return x - 1/3

def calK_derivada(x):
    return 1

def eq(x):
    k = calK(x)
    j = calK_derivada(x)

    print("Valor de f(x) = ", k)
    print("Valor de f(x)' = ", j)
    
    res_final = x - (k/j)
    
    print("res final = ", res_final)
    print("Valor da funcao atual = ", calK(res_final))

eq(0.3)
