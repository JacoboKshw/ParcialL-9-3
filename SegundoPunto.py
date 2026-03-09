def clasificar(c):
    if c.isalpha():
        return "letra"
    elif c.isdigit():
        return "digito"
    else:
        return "otro"

transiciones = {
    "q0": {"letra": "q1", "digito": "qm", "otro": "qm"},
    "q1": {"letra": "q1", "digito": "q1", "otro": "qm"},
    "qm": {"letra": "qm", "digito": "qm", "otro": "qm"},
}

estados_acept = {"q1"}

def afd(cadena):
    estado = "q0"
    for c in cadena:
        simbolo = clasificar(c)
        estado = transiciones[estado][simbolo]
    return estado in estados_acept


print(afd('miVariable')) 
print(afd('abc123'))      
print(afd('Z'))          
print(afd('2variable'))   
print(afd('hola mundo'))  
print(afd('_var'))       
print(afd(''))            
