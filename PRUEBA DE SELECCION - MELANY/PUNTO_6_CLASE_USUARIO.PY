###Cree una clase usuario con: 
# propiedades: usuario, email
# Un método saludar() que devuelva: "Hola, me llamo [usuario]"
# Crea una instancia de la clase y llama al método saludar() .###

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def saludar(self):
        return f'Hola me llamo {self.name}'
    
mi_usuario = usuario('melany', 'melany@hotmail')
print(mi_usuario.saludar())
