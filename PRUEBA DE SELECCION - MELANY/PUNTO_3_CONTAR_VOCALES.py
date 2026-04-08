#Escriba una función que reciba una cadena de texto y devuelva la cantidad de vocales ( a, e, i, o, u ).

def contar_vocales(vocal):
    contador = 0         
    for letra in vocal:
        if letra in 'AaEeiIoUu':
            contador += 1  
    return contador

print(contar_vocales('melany'))  
