# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número decimal a operar:')
numero_1 = float(input())

print('Ingrese por consola el segundo número decimal a operar:')
numero_2 = float(input())

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)
print('Los numeros ingresados son:', numero_1, ',', numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
suma = numero_1 + numero_2

# Resta
resta = numero_1 - numero_2

# División
div = numero_1 / numero_2

# Multiplicación
multi = numero_1 * numero_2

# print de todos los resultados 
# Suma 
print('el resultado de sumar', numero_1, 'y', numero_2, 'es', suma )

# Resta
print('el resultado de restar', numero_1, 'y', numero_2, 'es', resta )

# división 
print('el resultado de dividir', numero_1, 'entre', numero_2, 'es', div )

# Multiplicación
print('el resultado de multiplicar', numero_1, 'por', numero_2, 'es', multi )

#Output
'''
Ingrese por consola el primer número decimal a operar:
1.5
Ingrese por consola el segundo número decimal a operar:
13.7
Los numeros ingresados son: 1.5 , 13.7
el resultado de sumar 1.5 y 13.7 es 15.2
el resultado de restar 1.5 y 13.7 es -12.2
el resultado de dividir 1.5 entre 13.7 es 0.10948905109489052
el resultado de multiplicar 1.5 por 13.7 es 20.549999999999997
'''
