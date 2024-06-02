lista=[]
Palabras=str(input("ingresar palabra (Enter para finalizar):"))
while Palabras!= "":
    lista.append(Palabras)
    Palabras=str(input("ingresar palabra (Enter para finalizar):"))
print("lista de palabras :")
print(lista)
def contar_vocales_consonantes(palabra):
    contador_vocales = 0
    contador_consonantes = 0
    for letra in palabra.lower():
        if letra in 'aeiou':
            contador_vocales+= 1
        if letra in 'bcdfghjklmnñpqrstvwxyz':
            contador_consonantes+= 1
    return contador_vocales, contador_consonantes
print("Lista de palabras con conteo de vocales y consonantes:")
for palabra in lista:
    vocales, consonantes = contar_vocales_consonantes(palabra)
    print(f"{palabra}: {vocales} vocales y {consonantes} consonantes")