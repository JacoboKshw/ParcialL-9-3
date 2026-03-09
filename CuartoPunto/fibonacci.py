import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 40
inicio = time.time()

resultado = fibonacci(n)

fin = time.time()
tiempo = fin - inicio

print(f"fibonacci({n}) = {resultado}")
print(f"Tiempo: {tiempo:.4f} segundos")
