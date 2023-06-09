# FUNCIONES INTERMEDIAS

# 1. Actualizar valores en diccionarios y listas:
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# estos print para ver los resultados iniciales y comparar con los cambios!
print(x)
print (directorio_deportes)

print("__________________________")

# 1.1 Cambia el valor 10 en x a 15
x[1][0] = 15 #esto hace que el index 0 del index 1 de x tome el valor de 15
print(x)


print("__________________________")



# 1.2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant' #esto hace que solo cambie el last_name del index 0 de estudiantes
print(estudiantes)


print("__________________________")



# 1.3 En el directorio_deportes, cambia "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés' # esto hace que solo cambie el index 0 solo de futbol
print(directorio_deportes)


print("__________________________")


# 1.4 Cambia el valor 20 en z a 30
z[0]['y'] = 30
print(z)

print("_______________________________________")
print("___________sig ejercicio_______________")
print("_______________________________________")


# 2. Iterar a través de una lista de diccionarios:
def iterateDictionary(some_list):
    for student_dict in some_list:
        output = ""
        for key, value in student_dict.items():
            output += f'{key} - {value}, '
        print(output.rstrip(', '))  # con output.restrip le pido que imprima una versión de la cadela en la variable output sin las comas y el espacio

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(estudiantes)


print("_______________________________________")
print("___________sig ejercicio_______________")
print("_______________________________________")

# 3. Obtener valores de una lista de diccionarios: 
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)


print("_______________________________________")
print("___________sig ejercicio_______________")
print("_______________________________________")


# 4. Iterar a través de un diccionario con valores de lista:
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for item in value:
            print(item)
        print()

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)


print("_______________________________________")
print("________________FINAL__________________")
print("_______________________________________")
