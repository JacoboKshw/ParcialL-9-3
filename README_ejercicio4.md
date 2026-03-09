# Comparacion de rendimiento: C vs Python

Compara un lenguaje compilado (C) y uno interpretado (Python) usando Fibonacci recursivo.

## Archivos
- `fibonacci.c` — version en C
- `fibonacci.py` — version en Python

## Compilar y ejecutar
```
gcc fibonacci.c -o fibonacci
./fibonacci
python3 fibonacci.py
```

## Resultados
| Lenguaje | Tiempo     |
|----------|------------|
| C        | 0.86 seg   |
| Python   | 14.87 seg  |

C es ~17 veces mas rapido porque compila directo a codigo maquina.
Python interpreta cada instruccion en tiempo de ejecucion.
