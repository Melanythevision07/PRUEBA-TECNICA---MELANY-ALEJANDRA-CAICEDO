#Escriba una función que filtre y devuelva los usuarios que tienen al menos 18 años y están activos ( is_active es true ).
 
def filtro_usuarios(usuarios):
    resultado = []
    for usuario in usuarios:
        if usuario ['age'] >= 18 and usuario ['is_active']:
            resultado.append(usuario)
    return resultado
    
usuarios = [
    {"name": "Alicia", "age": 22, "email": "alicia@ejemplo.com", "is_active": True},
    {"name": "Bruno", "age": 17, "email": "bruno@ejemplo.com", "is_active": True},
    {"name": "Carlos", "age": 19, "email": "carlos@ejemplo.com", "is_active": False},
    {"name": "Diana", "age": 30, "email": "diana@ejemplo.com", "is_active": True}
]

print(filtro_usuarios(usuarios))