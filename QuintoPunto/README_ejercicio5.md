# Fibonacci 

Calcula la secuencia de Fibonacci usando ANTLR4 con Python.

## Archivos
- `Fibonacci.g4` — gramatica ANTLR
- `main.py` — programa principal


## Generar el parser desde la gramatica
```
antlr4 -Dlanguage=Python3 Fibonacci.g4
```
Esto genera: `FibonacciLexer.py`, `FibonacciParser.py`, `FibonacciListener.py`

## Ejecutar
```
python3 main.py
```

## Ejemplo
```
Ingrese la expresion:
FIBO(20) = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
```
