#Escriba una función que reciba una lista/array y devuelva una nueva sin elementos duplicados (preservando el orden original).

def eliminar_duplicados(objetos):
    nueva = []
    for cosas in objetos:
        if cosas not in nueva:
            nueva.append(cosas)
    return nueva

print(eliminar_duplicados([1, 2, 2, 3, 1]))