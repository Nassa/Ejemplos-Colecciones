#Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
#Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función
#reduce.

from functools import reduce
def digitos_a_numeros(digitos):
    return reduce(lambda x,y:x*10 + y, digitos)
print(digitos_a_numeros([4, 3, 9, 2]))