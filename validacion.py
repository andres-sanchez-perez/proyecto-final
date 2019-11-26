while True:
    print("menu\n1 para ingresar nueva ficha\n2 para buscar una ficha medica\n")
    opcion3=str(input("ingrese una opcion:"))
    if(opcion3.isdigit()==True):
        opcion3_int=int(opcion3)
        if(opcion3>0):
            break
        else:
            print("ingrese una opcion valida")
            wait_for("presione una tecla para continuar")
            os.system("clear")
           
## el .isdigit(), verifica si el string es numerico, .isalpha() verifica si el string es alfabetico.##
