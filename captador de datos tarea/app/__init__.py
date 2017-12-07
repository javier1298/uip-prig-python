if __name__ == '__main__':
    contador = 0
    print("bienvenido al centr de captacion de datos")
    print("ahora elige una opcion para continuar")
while True:
    opc = print("\nopciones \n 1-) agregar colaborador \n 2-) eliminar colaborador")
    opc = input()
    if opc == "1":
       archivo = open("datos.txt" , "a")
       ced = input("escribe tu cedula: ")
       nom = input("escribe tu nombre: ")
       dep = input("departamento: ")
       poc = input("cual es tu posicion: ")
       sal = input("escribe tu salario: ")

       archivo.write("  ")
       archivo.write("[ ")
       archivo.write(ced)
       archivo.write(": ")
       archivo.write(nom)
       archivo.write(", ")
       archivo.write(dep)
       archivo.write(", ")
       archivo.write(poc)
       archivo.write(", ")
       archivo.write(sal)
       archivo.write(" ]")
       archivo.write("\n")
       archivo.close()
    elif opc == "2":
       print("usted ha elegido eliminar a un colaborador:")
       input("escriba su cedula: ")


