import calendar
import sys
import os

def paciente(opcion):
    ingresomatrizpacientes()

def inventario(opcion):
    ingresoelemento()
        
def facturacion(opcion):
    while True:
        print("menu\n1 para crear nueva factura\n2 para volver al menu principal")
        opcion4=int(input("ingrese su opcion:"))
        if (opcion4==1):
            matrizfactura()
        else:
            break

def calendario(opcion):
    F=int(input("ingrese el mes que quiere mostrar"))
    cal = calendar.month(2020, F)
    print ("Aquí está el calendario:", cal)
    pause()

def ingresomatrizpacientes():
    while True:
        while True:
            print("menu\ningrese 1 para ingresar nueva ficha\ningrese 2 para buscar una ficha medica\ningrese 3 para volver al menu principal")
            opcion3=str(input("ingrese una opcion:"))
            if(opcion3.isdigit()==True):
                opcion3_int=int(opcion3)
                if(opcion3_int>0):
                    break
            else:
                print("ingrese una opcion valida")
                pause()
                os.system("clear")
            
            
        if(opcion3_int==1):
            n=10
            m=6
            s=1
            a=[]
            for i in range(n):
                a.append([])
                for j in range(m):
                    if(s==1):
                        q="un nombre"
                        p=validacionalfabetica(q)
                    if(s==2):
                        q="una edad"
                        p=validacionnumerica(q)
                    if(s==3):
                        q="un genero"
                        p=validacionalfabetica(q)
                    if(s==4):
                        while True:
                            p=str(input("ingrese la cedula del paciente:"))
                            if(p.isdigit()==True):
                                if(len(p)==10):
                                    break
                            else:
                                print("ingrese una cedula valida")
                                wait_for("presione una tecla para continuar")
                                os.system("clear")
                    if(s==5):
                        q="un diagnostico"
                        p=validacionalfabetica(q)
                    if(s==6):
                        p=input("ingrese el tratamiento aqui:")
                    a[i].append(p)
                    s=s+1
                print(a)
                pause()
                print("si quiere ingresar otra ficha presiones cualquier boton\ncaso contrario presione 1")
                desicion=int(input("ingrese su desicion aquí:"))
                if(desicion==1):
                    break

    
        
def ingresoelemento():
    while True:
        while True:
            print("menu\ningrese 1 para ingresar un nuevo prodcuto\ningrese 2 para buscar un prodcuto\ningrese 3 para volver al menu principal")
            opcion4=str(input("ingrese una opcion:"))
            if(opcion4.isdigit()==True):
                opcion4_int=int(opcion4)
                if(opcion4_int>0):
                    break
            else:
                print("ingrese una opcion valida")
                pause()
                os.system("clear")
        if(opcion4_int==1):
            n=10
            m=4
            s=1
            a=[]
            for i in range(n):
                a.append([])
                for j in range(m):
                    if (s==1):
                        p=int(input("ingrese el numero identificador del producto que ingresara:"))
                    if (s==2):
                        p=str(input("ingrese el nombre del producto que ingresara:"))
                    if (s==3):
                        p=str(input("ingrese el tipo de producto que ingresara:"))
                    if (s==4):
                        p=int(input("ingrese la cantidad del producto que tiene:"))
                    a[i].append(p)
                    s=s+1
                print(a)
                pause()
                s=1
                print("si quiere ingresar otro producto presione cualquier tecla\ncaso contrario presione 1")
                desicion=int(input("ingrese su desicion aqui:"))
                if(desicion==1):
                    break
def matrizfactura():
    acu=0
    n=10
    m=2
    s=1
    a=[]
    for i in range(n):
        a.append([])
        for j in range(m):
            if (s==1):
                p=str(input("ingrese procedimiento hecho:"))
            elif(s==2):
                p=int(input("ingrese el valor del procedimiento:"))
                acu=acu+p
            a[i].append(p)
            s=s+1 
        print(a)
        pause()
        s=1    
        print("¿Desea ingresar otro procediemiento?\nen caso de serlo presione cualquier boton\ncaso contrario presione 1")
        desicion=int(input("ingrese su desicion:"))
        if(desicion==1):
            break
    print(a)
    subtotal=acu
    print("el subtotal es:",subtotal)
    IVA=subtotal*0.12
    print("El valor del IVA es:",IVA)
    total=subtotal+IVA
    print("el costo total de los procedimientos es:",total)
    pause()
    
def validacionalfabetica(nombre):
    while True:
        print("ingrese",nombre,"del paciente\n")
        dato=input("ingrese aqui el dato pedido:")
        if(dato.isalpha()==True):
            break
        else:
            print("ingrese",nombre,"valido")
            pause()
            os.system("clear")
    return dato

def validacionnumerica(nombre):
    while True:
        print("ingrese",nombre,"del paciente\n")
        dato=input("ingrese el dato pedido aqui:")
        if(dato.isdigit()==True):
            dato_int=int(dato)
            if(dato_int>0):
                break
        else:
            print("ingrese",nombre,"valido")
            pause()
            os.system("clear")
    return dato_int

def pause():
    pause=input("presione enter para continuar")##lo siguiente es el presione enter para continuar sin tener que usar la libreria termios, ya que esta libreria solo existe en UNIX,linux y onlinegdb##

while True:
    print("menu principal\n1 para pacientes\n2 para inventario\n3 para facturacion\n4 para calendario\n5 para salir\n")
    opcion=int(input("ingrese su opcion:"))
    if (opcion==1):
        paciente(opcion)
    
    elif (opcion==2):
        inventario(opcion)
        
    elif (opcion==3):
        facturacion(opcion)
        
    elif (opcion==4):
        calendario(opcion)
        
    if(opcion>=5):
        break


