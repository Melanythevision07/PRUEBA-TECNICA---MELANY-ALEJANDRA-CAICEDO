# PRUEBA-TECNICA---MELANY-ALEJANDRA-CAICEDO

Solución a los 10 ejercicios de Python solicitados para el Contrato de Aprendizaje SENA.

## Cómo ejecutar los ejercicios

Cada ejercicio se puede correr de forma individual con el siguiente comando:

```bash
python NOMBRE_DEL_ARCHIVO.py



## PUNTO 1.
cree una funcion llamada suma_lista con el argumento numeros.
En el return use sum() para que sume todos los elementos del argumento numeros. finalmente print llama a la funcion junto con la lista de numeros que queremos sumar.

## PUNTO 2.
Definí una función llamada par_o_impar con el argumento digito. Creé una condicional que permite ver si un número es par o impar a través del residuo, si el residuo de un número dividido entre 2 es cero significa que es Par, de lo contrario es Impar. Luego el print llama a la función con el número que queremos consultar para que la consola nos muestre el resultado de si es par o impar.

## PUNTO 3.
Definí la función contar_vocales con el argumento vocal. Creé una variable llamada contador con valor inicial cero. Antes del for, para que pueda acumular. El for recorre letra por letra el argumento vocal, y la condicional verifica si cada letra está en la cadena 'aeiou'. Si se cumple el contador aumenta en uno. Al final return devuelve el contador y el print muestra el número total de vocales de la palabra ingresada.

## PUNTO 4.
cree una funcion llamada numero junto con su argumento llamado mayor, el return emplea una funcion llamada max() que sirve para buscar el numero mayor en una lista de numeros que le entreguemos, creo una variable llamada mayor que es la que contiene la lista de numeros y luego empleo un print que llama a la funcion junto con la lista llamada mayor.

## PUNTO 5.
Definí una función llamada eliminar_duplicados con el argumento objetos. Creé una lista vacía llamada nueva donde irán los elementos sin repetir. El for recorre cada elemento del argumento objetos llamándolo cosas temporalmente. El if evalúa si cosas no está en la lista nueva — si no está lo agrega con append. El return devuelve la lista nueva y el print llama la función con la lista que queremos evaluar.

## PUNTO 6.
Creamos una clase usuario que funciona como plantilla para crear objetos con información. El init toma los datos y los guarda en el objeto usando self, que relaciona la información con ese usuario específico — self.name guarda el nombre y self.email guarda el correo. Definí otra función llamada saludar con self como argumento, que devuelve un f-string con 'Hola me llamo' junto al self.name. Creé una instancia llamada mi_usuario con nombre y email predeterminados, y el print llama al método saludar a través de mi_usuario.

## PUNTO 7.
cree la funcion es_contraseña_segura con el argumento contraseña, seguido en la proxima linea por un if que trae un len que cuenta los caracteres de la contraseña que queremos ingresar, si es mayor o igual a 8 y any sirve para evaluar si cualquier caracter del argumento tiene mayusc o minusc esto debe de ir junto con un c.isupper evaluando en contraseña, lo mismo con c.islower, any tambien evalua isdigit y tambien evalua los caracteres especiales, todo en esta funcion deve de ir relacionado con el conector logico and ya que todas las funciones se deben cumplir a la vez para que el resultado sea True, si cumple la funcion deavuelve True, si no devuelve False, creamos la variable contraseña que va a almacenar la contraseña que pediremos al usuario, y el print llama a la funcion pasandole la variable contraseña que el usuario ingreso.

## Punto 8.
Creé una función llamada palabra con el argumento inicial. La variable palabras usa split() para separar la cadena de texto en palabras individuales. La variable resultado toma la primera palabra desde el índice 0 tal cual, y con join() une el resto de palabras desde el índice 1 en adelante, donde capitalize() pone en mayúscula la primera letra de cada una. El return devuelve el resultado y el print muestra la función con la cadena que deseemos convertir a camelCase.

## Punto 9.
Creé la función filtro_usuarios con el argumento usuarios. Creé una lista vacía llamada resultado. El for recorre cada usuario de la lista y el if evalúa si su edad es mayor o igual a 18 y si is_active es True — si cumple ambas condiciones append agrega ese usuario a la lista resultado. Al terminar el for el return devuelve resultado. Luego creamos la lista de usuarios a evaluar y el print llama la función con esa lista para mostrar los usuarios que cumplen las condiciones.

## Punto 10.
"Creé una función llamada calificacion con el argumento nota. Creé una lista vacía llamada notas donde irán los estudiantes con mejor promedio. El for recorre cada elemento de nota y el if evalúa si el score es mayor o igual a 85 — si cumple append agrega ese estudiante a la lista notas. Al terminar el for el return devuelve la lista notas. Fuera de la función creamos la lista de estudiantes a evaluar y el print llama la función con esa lista para mostrar los que cumplen la condición."

