import re

testo = "Ciao,ciao! Come stai?Stai bene?"
#rimuovo la punteggiatura da "testo"
testo_1 = re.sub("\,|!|\?"," " , testo)

print(testo_1)

print("\n")
      
#trasformo la stringa senza punteggiatura in un array
testo_2 = testo_1.split()

print(testo_2)

print("\n")

#creo un dizionario
diz = {}

#creo un loop for per ogni parola nell' array

for p in testo_2:
    parola = p.lower()
    if parola in diz:
        diz[parola] += 1
    else:
        diz[parola] = 1

#

print(diz)



  

    

   














