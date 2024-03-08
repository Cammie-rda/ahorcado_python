#Juego del Ahorcado
#Definir una palabra
#Número definido de intentos
#Pedir al usuario que ingrese una letra a la vez
#Resultado de acierto o perdida

def ahorcado():
    #Definimos palabra secreta
    palabra_secreta="computador"
    letras_adivinadas=[]
    #Lista para almacenar las letras que concuerden con mi palabra
    intentos=5 #número de intentos

    while intentos> 0:
        palabra_mostrada= ""
        for letra in palabra_secreta:
       
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else: 
                palabra_mostrada +="_ "
        
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
                print("Haz adivinado la palabra")
                break
            #pedir al usuario una letra
        letra_usuario=input("Ingrese una letra:")

            #verificar si la letra ha sido adivinada en letras adivinadas
        if letra_usuario in letras_adivinadas:
                print("Ya has adivinado esa letra")
                continue
        if letra_usuario in palabra_secreta:
                print("Bien tu letra esta en la palabra")
                letras_adivinadas.append(letra_usuario)
        else: 
                print("Incorrecto, pierdes un intento te quedan" + intentos)
        if intentos == 0:
                print("Lo siento, has agotado todos los intentos, la palabra era "
                 + palabra_secreta)

#Llamar a la función
ahorcado()