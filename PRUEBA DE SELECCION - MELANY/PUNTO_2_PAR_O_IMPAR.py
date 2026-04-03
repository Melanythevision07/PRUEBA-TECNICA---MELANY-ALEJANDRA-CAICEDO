#Escriba una función que reciba un número y devuelva "Par" si es par, o "Impar" si es impar.

def par_o_impar(digito):
    if digito % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
print(par_o_impar(5))    
print(par_o_impar(2))   
print(par_o_impar(11))   
print(par_o_impar(-19))  