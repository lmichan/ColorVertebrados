import random

ciclo=True
jugar=input("quieres tirar los dados s/n?")
while ciclo:
    if jugar=="s":
        a=random.choice([1,2,3,4,5,6])
        b=random.choice([1,2,3,4,5,6])
        print("==================================")
        print("el primer dado cayó:",a,"\n")
        print("el segundo dado cayó:",b,"\n")
        print("la suma de ambos es:",a+b)
        print("==================================")
        print("quieres tirar de nuevo? s/n")
        
        jugar=input(" ")
    elif jugar== "n":
        ciclo=False       
    else:
        jugar=input("por favor selecciona una opcion válida s/n")
        
print("gracias por jugar \nHasta pronto")
input("prueba 2 repositorio")
