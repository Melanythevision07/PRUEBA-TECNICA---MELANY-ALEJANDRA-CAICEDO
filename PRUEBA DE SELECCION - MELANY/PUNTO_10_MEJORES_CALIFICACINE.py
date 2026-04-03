#Escriba una función que devuelva a los estudiantes con una calificación mayor o igual a 85.
def calificacion(nota):
    notas = []
    for calificaciones in nota:
       if calificaciones ['score'] >= 85:
            notas.append(calificaciones)
    return notas
nota = [
{ "name": "Juan", "score": 88, "grade_level": 10 },
{ "name": "Luisa", "score": 76, "grade_level": 11 }, 
{ "name": "Laura", "score": 92, "grade_level": 12}
]
print(calificacion(nota))
        

