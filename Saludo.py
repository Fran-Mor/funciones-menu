def menu():
    print("1). Saludar")
    print("2). Despedirse.")
    
    
while True:
    menu()
    opc=int(input("Elige una opcion: "))

    if opc == 1:
        print("Hola")
    elif opc == 2:
        print("Chao")
    else:
        print("Su opcion no es valida")
    