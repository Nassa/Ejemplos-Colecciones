#Utilizar la función incorporada map() para crear una función que retorne una lista con la
#longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena
#de texto y retornará una lista.

def longitud_palabras(frase):
    palabra_len=list(map(len,frase.split()))
    return palabra_len
print(longitud_palabras('Hola Luis, como estas?'))