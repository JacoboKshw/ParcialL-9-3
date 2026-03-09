TRANSICIONES = {
    'q0': {
        'p': 'q1', 'q': 'q1', 'b': 'q1', 'r': 'q1',
        'k': 'q2',
        'n': 'fin',
    },
    'q1': {
        'n': 'fin', 'b': 'fin', 'r': 'fin', 'q': 'fin',
        'k': 'q3',
    },
    'q2': {
        'b': 'q4',
        'n': 'fin', 'p': 'fin',
        '1': 'fin', '2': 'fin', '3': 'fin', '4': 'fin',
        '5': 'fin', '6': 'fin', '7': 'fin', '8': 'fin',
    },
    'q3': {
        'b': 'q4', 'n': 'fin', 'p': 'fin',
        '1': 'fin', '2': 'fin', '3': 'fin', '4': 'fin',
        '5': 'fin', '6': 'fin', '7': 'fin', '8': 'fin',
    },
    'q4': {
        'p': 'fin',
        '1': 'fin', '2': 'fin', '3': 'fin', '4': 'fin',
        '5': 'fin', '6': 'fin', '7': 'fin', '8': 'fin',
    },
    'fin': {
        '1': 'fin', '2': 'fin', '3': 'fin', '4': 'fin',
        '5': 'fin', '6': 'fin', '7': 'fin', '8': 'fin',
    },
}

def afd(cadena):
    estado = 'q0'
    for letra in cadena.lower():
        if letra not in TRANSICIONES.get(estado, {}):
            return False
        estado = TRANSICIONES[estado][letra]
    return estado == 'fin'


print(afd('kbp'))
print(afd('qn'))
print(afd('pp'))
print(afd('kbp'))  
print(afd('qn'))   
print(afd('k4'))    
print(afd('kn'))    
print(afd('kb3')) 
print(afd('qk4'))   
print(afd('pn'))    
print(afd('n'))     
print(afd(''))      
    
