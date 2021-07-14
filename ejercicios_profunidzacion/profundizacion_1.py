# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('Ingresa dos numeros reales')

print('Número 1:')
numero_1 = int(input())

print('Número 2:')
numero_2 = int(input())

print('Los números ingresados son:', numero_1, 'y', numero_2)

# Operaciones

# Suma
suma = numero_1 + numero_2  

# Resta
resta = numero_1 - numero_2

# Multiplicación
multi = numero_1 * numero_2

# Divición
div = numero_1 / numero_2

# Potencia
pot = numero_1 ** numero_2

# Resultados

# Suma 
print('La suma entre', numero_1,'y', numero_2, 'es', suma)

# resta 
print('La resta entre', numero_1,'y', numero_2, 'es', resta)

# Multiplicación 
print('El producto entre', numero_1,'y', numero_2, 'es', multi)

# División 
print('El Cociente de', numero_1,'entre', numero_2, 'es', div)

# División 
print('El valor de', numero_1,'elevado a la', numero_2, 'es', pot)