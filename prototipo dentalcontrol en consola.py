import calendar
import sys
import os

def paciente(opcion):
    ingresomatrizpacientes()

def inventario(opcion):
    ingresoelemento()
        
def facturacion(opcion):
    while True:
        while True: 
            print("menu\n1 para crear nueva factura\n2 para volver al menu principal")         
            opcion5=input("ingrese su opcion:")
            if(opcion5.isdigit()==True):
                opcion5_int=int(opcion5)
                if(opcion5_int>0):
                    break
        if (opcion5_int==1):
            matrizfactura()
        elif(opcion_5==2):
            break
        else:
            print("ingrese una opcion valida")
            pause()

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
                os.system("cls")
            
            
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
                        p=validacioncedula()
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
                q="desicion aqui:"
                desicion=validacionnumerica(q)
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
                os.system("cls")
        if(opcion4_int==1):
            n=10
            m=4
            s=1
            a=[]
            for i in range(n):
                a.append([])
                for j in range(m):
                    if (s==1):
                        q="el identificador del producto:"
                        p=validacionnumerica(q)
                    if (s==2):
                        q="el nombre del prodcuto:"
                        p=validacionalfabetica(q)
                    if (s==3):
                        q="el tipo de producto:"
                        p=validacionalfabetica
                    if (s==4):
                        q="cantidad de producto que tiene:"
                        p=validacionnumerica(q)
                    a[i].append(p)
                    s=s+1
                print(a)
                pause()
                print("si quiere ingresar otro producto presione cualquier tecla\ncaso contrario presione 1")
                q="desicion aqui:"
                desicion=validacionnumerica(q)
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
                q="el procedimiento hecho"
                p=validacionalfabetica(q)
            elif(s==2):
                q="el valor del procedimiento"
                p=validacionnumerica(q)
                acu=acu+p
            a[i].append(p)
            s=s+1 
        print(a)
        pause()
        s=1    
        print("¿Desea ingresar otro procediemiento?\nen caso de serlo presione cualquier boton\ncaso contrario presione 1")
        q="desicion aqui:"
        desicion=validacionnumerica(q)
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
            print("ingrese un dato valido")
            pause()
            os.system("cls")
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
            print("ingrese un dato valido")
            pause()
            os.system("cls")
    return dato_int

def validacioncedula():
    while True:
        dato=str(input("ingrese la cedula del paciente:"))
        if(dato.isdigit()==True):
            if(len(dato)==10):
                break
            else:
                print("ingrese una cedula de 10 digitos")
        else:
            print("ingrese una cedula valida")
            pause()
            os.system("cls")
    return dato

def pause():
    pause=input("presione enter para continuar")##lo siguiente es el presione enter para continuar sin tener que usar la libreria termios, ya que esta libreria solo existe en UNIX,linux y onlinegdb##

while True:
    while True:
        print("menu principal\n1 para pacientes\n2 para inventario\n3 para facturacion\n4 para calendario\n5 para salir\n")
        opcion=input("ingrese su opcion:")
        if(opcion.isdigit()==True):
            opcion_int=int(opcion)
            if(opcion_int>0):
                break
        else:
            print("ingrese un dato valido")
            pause()
            os.system("cls")
            
    if (opcion_int==1):
        paciente(opcion_int)
    
    elif (opcion_int==2):
        inventario(opcion_int)
        
    elif (opcion_int==3):
        facturacion(opcion_int)
        
    elif (opcion_int==4):
        calendario(opcion_int)
        
    if(opcion_int>=5):
        break
