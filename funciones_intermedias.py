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

# 1. Cambia el valor 10 en x a 15
x[1][0] = 15 #esto hace que el index 0 del index 1 de x tome el valor de 15
print(x)


print("__________________________")



# 2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = 'Bryant' #esto hace que solo cambie el last_name del index 0 de estudiantes
print(estudiantes)


print("__________________________")



# 3. En el directorio_deportes, cambia "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = 'Andrés' # esto hace que solo cambie el index 0 solo de futbol
print(directorio_deportes)


print("__________________________")


# 4. Cambia el valor 20 en z a 30
z[0]['y'] = 30
print(z)
