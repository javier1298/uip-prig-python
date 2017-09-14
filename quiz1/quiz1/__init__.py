P = "casa"
print ("Tienes 3 oportinidades para decubrir la palabra secreta")
r = input("escribe la palabra:")
for i in range (3):
 if r == P:
        print("felicidades, ganaste")
 elif r != P:
        r = input("intentalo de nuevo")
        break








