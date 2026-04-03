#Escriba una función que convierta una oración a formato camelCase.
def palabra(inicial):
    palabras = inicial.split()
    resultado = palabras [0] + "".join(p.capitalize() for p in palabras [1:])
    return resultado
print(palabra('hola mundo otra vez'))
