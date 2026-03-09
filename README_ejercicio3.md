# Calculadora de raiz cuadrada

Usa Flex y Bison para leer expresiones y calcular la raiz con Newton-Raphson.

## Archivos
- `calculadora.l` — lexer (Flex)
- `calculadora.y` — parser (Bison)
- `entrada.txt` — pruebas

## Compilar y ejecutar
```
flex calculadora.l
bison -d calculadora.y
cc calculadora.tab.c lex.yy.c -o calculadora -lm
./calculadora < entrada.txt
```

## Ejemplo
entrada.txt:
```
sqrt(144)
sqrt(25)
```
Salida:
```
Raiz aproximada: 12.000000
Raiz aproximada: 5.000000
```
