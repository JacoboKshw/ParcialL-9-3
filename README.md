# Punto 1 y 2
Implementación de dos Autómatas Finitos Deterministas (AFD)

---

## PrimerPunto.py


**Estados:**
- `q0` → inicio
- `q1` → después de `p, q, b, r`
- `q2` → después de `k` desde el inicio
- `q3` → después de `k` desde q1
- `q4` → después de `b` desde q2 o q3
- `fin` → estado de aceptación

**Ejemplos:**
```
afd('kbp')  → True
afd('qn')   → True
afd('pp')   → False
afd('k4')   → True
afd('')     → False
```

---

## SegundoPunto.py

Reconoce identificadores válidos según la expresión regular `[A-Za-z][A-Za-z0-9]*`.

Un ID válido empieza con una letra, seguida de cero o más letras o dígitos.

**Estados:**
- `q0` → inicio
- `q1` → leímos al menos una letra (aceptación)
- `qm` → carácter inválido

**Ejemplos:**
```
afd('miVariable') → True
afd('abc123')     → True
afd('2variable')  → False
afd('hola mundo') → False
afd('')           → False
```

---

## Cómo ejecutar

```bash
python PrimerPunto.py
python SegundoPunto.py
```
