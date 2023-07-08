points = 0
# depende de los puntos que haya, la contraseña es más o menos segura

# Añadir tambien longitud de contraseña

input('Hola, te voy a decir cómo de fácil de adivinar es tu contraseña. Pulsa ENTER para continuar.')
password = input('Introduce tu contraseña:')

if password == None:
    print('Lo siento, no puedes dejar este campo vacío.')
    password = input('Introduce tu contraseña:')

for character in password: # uppercase letters
    if 'A' <= character <= 'Z':
        points += 1
        break

for character in password: # lowercase letters   
    if 'a' <= character <= 'z':
        points += 1
        break

for character in password: # numbers        
    if '0' <= character <= '9':
        points += 1
        break

for character in password: # special characters
    if ' ' <= character <= '/' or ':' <= character <= '@' or '[' <= character <= '`' or '{' <= character <= '~':
        points += 1
        break

# Problema: la parte de 'for' no hace absolutamente nada :/
# Con lo cual, la parte en la que te dice cómo de segura es la contraseña tampoco hace nada.

# for letter in capital_letters:
#     if letter in password:
#         points += 1

# for letter in small_letters:
#     if letter in password:
#         points += 1

# for number in numbers:
#     if number in password:
#         points += 1

# for character in special_characters:
#     if character in password:
#         points += 1

for x in range(5):
    print('Calculando...')

final_points = points * len(password)

if final_points <= 12:
    print('Tu contraseña es muy poco segura.')
elif final_points <= 24:
    print('Tu contraseña es poco segura.')
elif final_points <= 36:
    print('Tu contraseña es segura.')
elif final_points <= 48:
    print('Tu contraseña es muy segura.')
else:
    print('¡Tu contraseña es la hostia!')