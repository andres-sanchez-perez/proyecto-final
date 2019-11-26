import calendar
import sys
import termios

def wait_for(mess, *keys):
    file_descriptor = sys.stdin.fileno()
    old = termios.tcgetattr(file_descriptor)
    new = old[:]

    try:
        new[3] &= ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, new)
        print(mess, end="")
        while True:
            letra = sys.stdin.read(1)
            if not keys or letra in keys:
                print()
                break
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old)


def paciente(opcion):
    ingresomatrizpacientes()
def inventario(opcion):
    while True:
        print("menu\n1 para agregar un nuevo producto\n2 para buscar un producto\n3 para modificar un elemento\n4 para eliminar un producto\n5 para volver al menu principal")
        opcion3=int(input("ingrese su opcion:"))
        if (opcion3==1):
            ingresoelemento()
        elif (opcion3==2):
            buscarelemento()
        elif (opcion3==3):
            modificarelelemento()
        elif (opcion3==4):
            eliminarelemento()
        if(opcion3>=5):
            break

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
    wait_for("Presione una tecla para continuar")

def ingresomatrizpacientes():
    while True:
        while True:
            print("menu\ningrese 1 para ingresar nueva ficha\ningrese 2 para buscar una ficha medica\ningrese 3 para volver al menu principal")
            opcion3=str(input("ingrese una opcion:"))
            if(opcion3.isdigit()==True):
                if(opcion3>0):
                    opcion3_int=int(opcion3)
                    break
            else:
                print("ingrese una opcion valida")
                wait_for("presione una tecla para continuar")
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
                        p=str(input("ingrese el nombre del paciente:"))
                    if(s==2):
                        p=int(input("ingrese la edad del paciente:"))
                    if(s==3):
                        p=str(input("ingrese el genero del paciente:"))
                    if(s==4):
                        p=int(input("ingrese la cedula del paciente:"))
                    if(s==5):
                        p=str(input("ingrese el diagnostico del paciente:"))
                    if(s==6):
                        p=str(input("ingrese el tratamiento a seguir:"))
                    a[i].append(p)
                    s=s+1
                print(a)
                wait_for("Presione una tecla para continuar")
                print("si quiere ingresar otra ficha presiones cualquier boton\ncaso contrario presione 1")
                desicion=int(input("ingrese su desicion aquí:"))
                if(desicion==1):
                    break
        
def ingresoelemento():
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
        wait_for("Presione una tecla para continuar")
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
        wait_for("Presione una tecla para continuar")
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
    wait_for("Presione una tecla para continuar")
    


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

