###
# Escriba una función es_contraseña_segura(contraseña) que devuelva True si la contraseña cumple con lo siguiente:
# Tiene al menos 8 caracteres
# Contiene al menos una letra mayúscula
# Contiene al menos una letra minúscula
# Contiene al menos un dígito
# Contiene al menos un carácter especial (!@#$%^&*)###

def es_contraseña_segura(contraseña):
    if len(contraseña) >= 8 and  any(c.isupper() for c in contraseña) and any(c.islower() for c in contraseña) and any(c.isdigit() for c in contraseña) and any(c in '!@#$%^.&*' for c in contraseña):
        return(True)
    else:
        return(False)
    
contraseña = input('Ingrese una contraseña segura. ')
print(es_contraseña_segura(contraseña)) 
