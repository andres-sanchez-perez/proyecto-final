import calendar
import sys
import os
from colorama import init,Fore, Back, Style

init()

def inventario(opcion):
    ingresoelemento()
        
def facturacion(opcion,A):
    while True:
        while True: 
            print(Style.BRIGHT+"menu\n1 para crear nueva factura\n2 para volver al menu principal")         
            opcion5=input("ingrese su opcion:")
            if(opcion5.isdigit()==True):
                opcion5_int=int(opcion5)
                if(opcion5_int>0 and opcion5_int<=2):
                    os.system("cls")
                    break
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese 1 o 2"+Style.RESET_ALL)
                    pause()
                    os.system("cls")
        if (opcion5_int==1):
            matrizfactura(A)
        elif(opcion5_int==2):
            os.system("cls")
            break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            os.system("cls")
            pause()

def calendario(opcion):
    while True:
        F=input("ingrese el mes que quiere mostrar")
        if(F.isdigit()==True):
            F_int=int(F)
            if(F_int>=1 and F_int<=12):
                os.system("cls")
                cal = calendar.month(2020,F_int)
                print(Style.BRIGHT+"Aquí está el calendario:", cal)
                pause()
                os.system("cls")
                pause()
            else:
                print(Style.BRIGHT+Fore.RED+"ingrese un numero del 1 al 12"+Style.RESET_ALL)
                pause()
        print(Style.BRIGHT+Fore.RED+"Si quiere ingresar otro mes presione 1\nCaso contrario presione 2"+Style.RESET_ALL)
        q="desicion"
        desicion6=validaciondesicion(q)
        if(desicion6==1):
            break
            os.system("cls")
        elif(desicion6>2):
            print(Style.BRIGHT+Fore.RED+"Ingrese 1 o 2"+Style.RESET_ALL)
            os.system("cls")

def busquedaficha(a,cedula):
    while True:
        seguro=False
        for i in range(len(a)):
            for j in range(len(a[0])):
                if(cedula==a[i][j-3]):
                    print("\n\n",a[i])
                    pause()
                    os.system("cls")
                    seguro=True
                    break
            if(seguro==True):
                break
        if(seguro==True):
            break
def modificarficha(a,cedula):
    while True:
        seguro=False
        for i in range(len(a)):
            for j in range(len(a[0])):
                if(cedula==a[i][j-3]):
                    print("\n\n",a[i])
                    q="desicion"
                    print(Style.BRIGHT+Fore.YELLOW+"Si desea proceder a modificar la ficha presione 1\nsi quiere modificar otra ficha presione 2\npresione cualquier boton para cancelar"+Style.RESET_ALL)
                    desicion11=validaciondesicion(q)
                    os.system("cls")
                    if(desicion11==1):
                        a[i][4]=enfermedades()
                        k=a[i][4]
                        a[i][5]=tratamiento(k)
                        print("\n\n",a[i])
                        seguro=True
                        pause()
                        os.system("cls")
                        break
                    elif(desicion11==2):
                        w="cedula de identidad:"
                        cedula=w+" "+validacioncedula()
                        os.system("cls")
                        i=0
                    else:
                        os.system("cls")
                        seguro=True
                        break
            if(seguro==True):
                break
        if(seguro==True):
            break
def eliminarficha(a,cedula):
    while True:
        seguro=False
        for i in range(len(a)):
            for j in range(len(a[0])):
                if(cedula==a[i][j-3]):
                    print("\n\n",a[i])
                    q="desicion"
                    print(Style.BRIGHT+Fore.YELLOW+"Si desea proceder a eliminar la ficha presione 1\nsi quiere eliminar otra ficha presione 2\npresione cualquier boton para cancelar"+Style.RESET_ALL)
                    desicion10=validaciondesicion(q)
                    os.system("cls")
                    if(desicion10==1):
                        a.pop(i)
                        print("\n\n",a)
                        pause()
                        os.system("cls")
                        seguro=True
                        break
                    elif(desicion==2):
                        w="cedula de identidad:"
                        cedula=w+" "+validacioncedula()
                        os.system("cls")
                        i=0
                    else:
                        os.system("cls")
                        seguro=True
                        break
            if(seguro==True):
                break
        if(seguro==True):
            break
            
def ingresoelemento():
    while True:
        while True:
            print(Style.BRIGHT+"menu\ningrese 1 para ingresar un nuevo producto\ningrese 2 para buscar un producto\ningrese 3 imprimir los productos ingresados\ningrese 4 para volver al menu principal")
            opcion4=str(input("ingrese una opcion:"))
            os.system("cls")
            if(opcion4.isdigit()==True):
                opcion4_int=int(opcion4)
                if(opcion4_int>0):
                    os.system("cls")
                    break
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese un numero mayor a 0"+Style.RESET_ALL)
                    pause()
                    os.system("cls")
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
                pause()
                os.system("cls")
        if(opcion4_int==1):
            f=1
            n=10
            m=4
            s=1
            a=[]
            for i in range(n):
                a.append([])
                for j in range(m):
                    if (s==1):
                        p=f
                    if (s==2):
                        p=input(Style.BRIGHT+"ingrese el nombre del producto\n")
                        os.system("cls")
                    if (s==3):
                        p=listamateriales()
                    if (s==4):
                        q="cantidad de producto que tiene:"
                        p=validacionnumerica2(q)
                        os.system("cls")
                    a[i].append(p)
                    s=s+1
                print("\n\n",a)
                pause()
                print(Style.BRIGHT+Fore.YELLOW+"si quiere ingresar otro producto presione cualquier tecla\ncaso contrario presione 1"+Style.RESET_ALL)
                q="desicion"
                desicion=validaciondesicion(q)
                os.system("cls")
                if(desicion==1):
                    break
                s=1
                f=f+1
        elif(opcion4_int==2):
            while True:
                seguro=False
                while True:
                    print(Style.BRIGHT)
                    buscar=input("ingrese el identificador a buscar:")
                    os.system("cls")
                    if(buscar.isdigit()==True):
                        buscar_int=int(buscar)
                        if(buscar_int>0):
                            if(buscar_int<=n):
                                break
                        else:
                            init()
                            print(Style.BRIGHT+Fore.RED+"ingrese un numero mayor a 0"+Style.RESET_ALL)
                            os.system("cls")
                    else:
                        init()
                        print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
                        pause()
                        os.system("cls")
                for i in range(len(a)):
                    for j in range(len(a[0])):   
                        if(buscar_int==a[i][j]):
                            print(a[i])
                            while True:
                                print(Style.BRIGHT+"¿Que desea hacer con este producto?\ningrese 1 para modificar la cantidad del producto\ningrese 2 para eliminar producto")
                                q="desicion"
                                desicion4=validaciondesicion(q)
                                os.system("cls")
                                if(desicion4>0):
                                    if(desicion4<=2):
                                        break
                                else:
                                    init()
                                    print(Style.BRIGHT+Fore.RED+"ingrese una de las opciones disponibles"+Style.RESET_ALL)
                                    pause()
                                    os.system("clear")
                            if(desicion4==1):
                                q="cantidad de producto que tiene ahora:"
                                a[i][3]=validacionnumerica2(q)
                                print("\n\n",Style.BRIGHT+str(a[i]))
                                pause()
                                os.system("cls")
                                seguro=True
                                break
                            elif(desicion4==2):
                                a.pop(i)
                                print(a)
                                pause()
                                os.system("cls")
                                seguro=True
                                break
                    if(seguro==True):
                        break  
                print(Style.BRIGHT+Fore.YELLOW+"¿Desea buscar otro numero?\nsi es asi presione cualquier tecla\n caso contrario presione 1"+Style.RESET_ALL)
                q="desicion"
                desicion5=validaciondesicion(q)
                print(Style.BRIGHT)
                os.system("cls")
                if(desicion5==1):
                    break
        elif(opcion4_int==3):
            print(Style.BRIGHT+str(a))
            pause()
            os.system("cls")
        elif(opcion4_int==4):
            break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una de las opciones disponibles"+Style.RESET_ALL)
            os.system("cls")
    return a
def matrizfactura(g):
    m=2
    s=1
    a=[]
    w="cedula de identidad:"
    buscar=w+" "+validacioncedula()
    os.system("cls")
    seguro=False
    if(len(g)>1):
        for i in range(len(g)):
            for j in range(len(g[0])):
                if(buscar==g[i][j-3]):
                    h=g[i][5]
                    seguro=True
                    break
            if(seguro==True):
                break
    else:
        if(buscar==g[0][3]):
            h=g[0][5]
    for i in range(m):
        if (s==1):
            p=h
        elif(s==2):
            q="el valor del procedimiento en dolares"
            z=validacionnumerica2(q)
            os.system("cls")
            while True:
                v="el valor del procedimiento en centavos"
                b=validacionnumerica2(v)/100
                os.system("cls")
                if(b>0):
                    if(b<1):
                        break
                    else:
                        init()
                        print(Style.BRIGHT+Fore.RED+"ingrese un numero del 1 al 100"+Style.RESET_ALL)
                        os.system("cls")
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese un numero positivo"+Style.RESET_ALL)
                    os.system("cls")
            c="costo:"
            q=z+b
            p=c+str(q)
        a.append(p)
        s=s+1 
    print(a)
    subtotal=float(q)
    print("el subtotal es:",subtotal)
    IVA=subtotal*0.12
    l=round(IVA,2)
    print("El valor del IVA es:",l)
    total=subtotal+IVA
    d=round(total,2)
    print("el costo total de los procedimientos es:",d)
    pause()
    os.system("cls")

def validacionalfabetica2(nombre):
    while True:
        print(Style.BRIGHT+"ingrese",nombre,"\n")
        dato=input()
        if(dato.isalpha()==True):
            break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato
    
def validacionalfabetica(nombre):
    while True:
        print(Style.BRIGHT+"ingrese",nombre,"del PACIENTE:")
        dato=input()
        if(dato.isalpha()==True):
            break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato
def validaciongenero(nombre):
    while True:
        print(Style.BRIGHT+"ingrese",nombre,"del PACIENTE:")
        dato=input()
        if(dato.isalpha()==True):
            if(dato=="masculino" or dato=="femenino"):
                break
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese masculino o femenino"+Style.RESET_ALL)
                pause()
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato
def validaciondesicion(nombre):
    while True:
        print(Style.BRIGHT+Fore.YELLOW+"¿cual es su",nombre,"?"+Style.RESET_ALL)
        dato=input()
        if(dato.isdigit()==True):
            dato_int=int(dato)
            if(dato_int>0):
                break
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese un numero mayor a 0"+Style.RESET_ALL)
        elif(dato.isdigit()==False):
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato_int

def validacionnumerica2(nombre):
    while True:
        print(Style.BRIGHT+"ingrese",nombre,"\n")
        dato=input()
        if(dato.isdigit()==True):
            dato_int=int(dato)
            if(dato_int>0):
                break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato_int

def validacionnumerica(nombre):
    while True:
        print(Style.BRIGHT+"ingrese",nombre,"del PACIENTE:")
        dato=input()
        if(dato.isdigit()==True):
            dato_int=int(dato)
            if(dato_int>0):
                break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato_int

def validacioncedula():
    while True:
        print(Style.BRIGHT)
        dato=str(input("ingrese la cedula del paciente:"))
        if(dato.isdigit()==True):
            if(len(dato)==10):
                break
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese una cedula de 10 digitos"+Style.RESET_ALL)
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
    return dato
def listamateriales():
    s=[[1,"higiene dental"],[2,"exodoncia"],[3,"operatoria dental"],[4,"Periodoncia"],[5,"Ortodoncia"],[6,"Material quirurgico"]]
    print(Style.BRIGHT+"categorias de los productos:\n")
    for i in range(len(s)):
        for j in range(len(s[0])):
            print(s[i][j])
        print("\n")
    pause()
    while True:
        print(Style.BRIGHT)
        buscar=input("ingrese un numero entre la lista mostrada:")
        os.system("cls")
        if(buscar.isdigit()==True):
            buscar_int=int(buscar)
            if(buscar_int>0):
                if(buscar_int<=6):
                    break
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese un numero entre  1 y 6"+Style.RESET_ALL)
                    pause()
                    os.system("cls")
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
                pause()
                os.system("cls")
    seguro=False
    for i in range(len(s)):
        for j in range(len(s[0])):
            if(buscar_int==s[i][j]):
                dato=s[i][1]
                seguro=True
                break
        if(seguro==True):
            break
    return dato

def enfermedades():
    s=[[1,"caries"],[2,"gingivitis"],[3,"periodontitis"],[4,"cancer bucal"],[5,"halitosis"]]
    print(Style.BRIGHT+"lista de enfermedades")
    for i in range(len(s)):
        for j in range(len(s[0])):
            print(s[i][j],"\t")
        print("\n")
    pause()         
    while True:
        print(Style.BRIGHT+Fore.YELLOW+"si el diagnostico que busca esta dentro de la lista PRESIONE 1\nsi no esta en a lista PRESIONE 2 y escriba el diagnostico"+Style.RESET_ALL)
        print(Style.BRIGHT)
        q="desicion"
        desicion5=validaciondesicion(q)
        if(desicion5>0 and desicion5<=2):
            break
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese 1 o 2"+Style.RESET_ALL)
            pause()
    if(desicion5==1):
        while True:
            print(Style.BRIGHT)
            buscar=input("ingrese un numero entre la lista mostrada:")
            os.system("cls")
            if(buscar.isdigit()==True):
                buscar_int=int(buscar)
                if(buscar_int>0 and buscar_int<=5):
                    break
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese un numero entre  1 y 5"+Style.RESET_ALL)
                    pause()
                    os.system("cls")
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
                pause()
                os.system("cls")
        for i in range(len(s)):
            for j in range(len(s[0])):
                if(buscar_int==s[i][j]):
                    dato=s[i][1]
                    break
                else:
                    dato=None
            if dato is not None:
                break
    
    if(desicion5==2):
        print(Style.BRIGHT)
        dato=input("ingrese el diagnostico:")
        os.system("cls")
    return dato

def tratamiento(enfermedad):
    s=[["caries","empaste en el diente","endodoncia","extraccion del diente"],["gingivitis","limpieza dental","limpieza y restauracion dental"],["periodontitis","raspado","cirugia con colgajos","injerto de tejido blanco","injerto oseo"],["cancer bucal","extirpacion del tumor","diseccion de cuello"],["halitosis","enjuage bucal y dentrificos"]] 
    dato=None
    for i in range(len(s)):
        for j  in range(len(s[0])):
            if(enfermedad==s[i][0]):
                if(s[i][0]=="caries"):
                    while True:
                        print(Style.BRIGHT+"si las caries son leves ingrese 1\nsi las caries son de gravedad media ingrese 2\nsi son graves ingrese 3")
                        q="su desicion"
                        gravedad=validacionnumerica2(q)
                        os.system("cls")
                        if(gravedad<=3):
                            break
                        else:
                            init()
                            print(Style.BRIGHT+Fore.RED+"ingrese 1, 2 o 3"+Style.RESET_ALL)
                            pause()
                            os.system("cls")
                    if(gravedad==1):
                        dato=s[0][1]
                        break
                    elif(gravedad==2):
                        dato=s[0][2]
                        break
                    elif(gravedad==3):
                        dato=s[0][3]
                        break
                elif(s[i][0]=="gingivitis"):
                    while True:
                        q="si tiene los dientes con un ajuste deficiente o estan desalineados\nen caso de serlo ingrese 1\ncaso contrario ingrese 2"
                        respuesta=validacionnumerica2(q)
                        os.system("cls")
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                init()
                                print(Style.BRIGHT+Fore.RED+"ingrese 1 o 2"+Style.RESET_ALL)
                                pause()
                                os.system("cls")
                    if(respuesta==1):
                        dato=s[1][2]
                        break
                    elif(respuesta==2):
                        dato=s[1][1]
                        break
                elif(s[i][0]=="periodontitis"):
                    while True:
                        print(Style.BRIGHT+"si la periodontitis esta en una fase avanzada ingrese 1\ncaso contrario ingrese 2")
                        q="desicion"
                        respuesta=validacionnumerica2(q)
                        os.system("cls")
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                init()
                                print(Style.BRIGHT+Fore.RED+"ingrese 1 o 2"+Style.RESET_ALL)
                                pause()
                                os.system("cls")
                            
                    if(respuesta==1):
                        while True:
                            print(Style.BRIGHT+"si necesita incisiones minimas ingrese 1\nsi se ha perdido tejido de las encias ingrese 2\nsi el hueso ha sido destruido ingrese 3\n")
                            q="desicion"
                            respuesta2=validacionnumerica2(q)
                            os.system("cls")
                            if(respuesta2>0):
                                if(respuesta2<4):
                                    break
                                else:
                                    init()
                                    print(Style.BRIGHT+Fore.RED+"ingrese 1, 2 o 3"+Style.RESET_ALL)
                                    pause()
                                    os.system("cls")
                                
                        if(respuesta2==1):
                            dato=s[2][2]
                            break
                        elif(respuesta2==2):
                            dato=s[2][3]
                            break
                        elif(respuesta2==3):
                            dato=s[2][4]
                            break
                    elif(respuesta==2):
                        dato=s[2][1]
                        break
                elif(s[i][0]=="cancer bucal"):
                    while True:
                        print(Style.BRIGHT+"si se extendio al cuello ingrese 1\ncaso contrario ingrese 2")
                        q="desicion"
                        respuesta=validacionnumerica2(q)
                        os.system("cls")
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                init()
                                print(Style.BRIGHT+Fore.RED+"ingrese 1 o 2"+Style.RESET_ALL)
                                pause()
                                os.system("cls")
                    if(respuesta==1):
                        dato=s[3][2]
                        break
                    elif(respuesta==2):
                        dato=s[3][1]
                        break
                elif(s[i][0]=="halitosis"):
                    dato=s[4][1]
            
    if(dato==None):
        print(Style.BRIGHT)
        dato=input("ingrese el tratamiento a realizar:")
        os.system("cls")
    return dato
                    
                   
def pause():
    print(Style.BRIGHT)
    pause=input("presione enter para continuar")##lo siguiente es el presione enter para continuar sin tener que usar la libreria termios, ya que esta libreria solo existe en UNIX,linux y onlinegdb##

while True:
    while True:
        print(Style.BRIGHT+"menu principal\n1 para pacientes\n2 para inventario\n3 para facturacion\n4 para calendario\n5 para salir\n")
        opcion=input("ingrese su opcion:")
        if(opcion.isdigit()==True):
            opcion_int=int(opcion)
            if(opcion_int>0 and opcion_int<=5):
                break
            else:
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese un numero mayor entre 1 y 5"+Style.RESET_ALL)
        else:
            init()
            print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
            pause()
            os.system("cls")
            
    if (opcion_int==1):
        while True:
            while True:
                print("ingrese 1 para ingresar una nueva ficha\ningrese 2 para modificar una ficha\ningrese 3 para eliminar una ficha\ningrese 4 para imprimir un fichar\ningrese 5 para volver al menu principal\n")
                opcion9=input("ingrese su opcion:")
                if(opcion9.isdigit()==True):
                    opcion9_int=int(opcion9)
                    if(opcion9_int>0 and opcion9_int<=5):
                        os.system("cls")
                        break
                    else:
                        init()
                        print(Style.BRIGHT+Fore.RED+"ingrese un numero entre 1 y 5"+Style.RESET_ALL)
                        os.system("cls")
                else:
                    init()
                    print(Style.BRIGHT+Fore.RED+"ingrese una opcion valida"+Style.RESET_ALL)
                    pause()
                    os.system("cls")
            if(opcion9_int==1):
                n=10
                m=6
                s=1
                a=[]
                for i in range(n):
                    a.append([])
                    for j in range(m):
                        if(s==1):
                            q="un nombre"
                            g=validacionalfabetica(q)
                            os.system("cls")
                            q="un apellido"
                            x=validacionalfabetica(q)
                            os.system("cls")
                            w="nombre y apellido:"
                            p=w+g+" "+x #--->esto concantena los strings, esto equivale a los comandos de: strcat(cad0," ");strcat(cad0,cad1);#
                        if(s==2):
                            q="una edad"
                            w="edad:"
                            p=w+" "+str(validacionnumerica(q))
                            os.system("cls")
                        if(s==3):
                            q="un genero,(masculino o femenino),"
                            w="genero:"
                            p=w+" "+validaciongenero(q)
                            os.system("cls")
                        if(s==4):
                            w="cedula de identidad:"
                            p=w+" "+validacioncedula()
                            os.system("cls")
                        if(s==5):
                            w="diagnostico:"
                            x=enfermedades()
                            p=w+" "+x
                            os.system("cls")
                        z=x
                        if(s==6):
                            w="tratamiento:"
                            c=tratamiento(z)
                            p=w+" "+c
                            os.system("cls")
                        a[i].append(p)
                        s=s+1
                    print(a)
                    pause()
                    s=1
                    os.system("cls")
                    print(Style.BRIGHT+Fore.YELLOW+"si quiere ingresar otra ficha presiones cualquier boton\ncaso contrario presione 1")
                    q="desicion"
                    desicion=validaciondesicion(q)
                    if(desicion==1):
                        break
                    os.system("cls")
                A=a
            if(opcion9_int==2):
                w="cedula de identidad:"
                buscar=w+" "+validacioncedula()
                os.system("cls")
                seguro=False
                for i in range(len(A)):
                    if(buscar==A[i][3]):
                        modificarficha(A,buscar)
                        seguro=True
                    if(seguro==True):
                        break
            if(opcion9_int==3):   
                w="cedula de identidad:"
                buscar=w+" "+validacioncedula()
                os.system("cls")
                seguro=False
                for i in range(len(A)):
                    if(buscar==A[i][3]):
                        eliminarficha(A,buscar)
                        seguro=True
                    if(seguro==True):
                        break
            elif(opcion9_int==4):
                w="cedula de identidad:"
                buscar=w+" "+validacioncedula()
                os.system("cls")
                seguro=False
                for i in range(len(A)):
                    if(buscar==A[i][3]):
                        busquedaficha(A,buscar)
                        seguro=True
                    if(seguro==True):
                        break
            elif(opcion9_int==5):
                os.system("cls")
                break
            elif(opcion9_int>5):
                init()
                print(Style.BRIGHT+Fore.RED+"ingrese una de las opciones disponibles\n"+Style.RESET_ALL)
                os.system("cls")
                pause()
    elif (opcion_int==2):
        inventario(opcion_int)
    elif (opcion_int==3):
        facturacion(opcion_int,A)
    elif (opcion_int==4):
        calendario(opcion_int)
        
    elif(opcion_int==5):
        os.system("cls")
        break
    else:
        init()
        print(Style.BRIGHT+Fore.RED+"ingrese una de las  opciones disponibles"+Style.RESET_ALL)
        os.system("cls")
        pause()

