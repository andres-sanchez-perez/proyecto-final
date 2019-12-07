import calendar
import sys
import os

def inventario(opcion):
    ingresoelemento()
        
def facturacion(opcion,A):
    while True:
        while True: 
            print("menu\n1 para crear nueva factura\n2 para volver al menu principal")         
            opcion5=input("ingrese su opcion:")
            if(opcion5.isdigit()==True):
                opcion5_int=int(opcion5)
                if(opcion5_int>0):
                    break
        if (opcion5_int==1):
            matrizfactura(A)
        elif(opcion5_int==2):
            break
        else:
            print("ingrese una opcion valida")
            pause()

def calendario(opcion):
    F=int(input("ingrese el mes que quiere mostrar"))
    cal = calendar.month(2020, F)
    print ("Aquí está el calendario:", cal)
    pause()

def ingresomatrizpacientes(a,cedula):
    while True:
        while True:
            print("menu\ningrese 1 para buscar una ficha medica\ningrese 2 para volver al menu principal")
            opcion3=str(input("ingrese una opcion:"))
            if(opcion3.isdigit()==True):
                opcion3_int=int(opcion3)
                if(opcion3_int>0):
                    if(opcion3_int<=3):
                        break
            else:
                print("ingrese una opcion valida")
                pause()
                os.system("cls")
            
        if(opcion3_int==1):
            while True:
                seguro=False
                for i in range(len(a)):
                    for j in range(len(a[0])):
                        if(cedula==a[i][j-3]):
                           print(a[i])
                           while True:
                               print("¿Que desea hacer con la ficha encontrada?\ningrese 1 para modificar dicha ficha\ningrese 2 para eliminarla\ningrese 3 cancelar")
                               opcion6=input("ingrese su desicion aqui:")
                               if(opcion6.isdigit()==True):
                                   opcion6_int=int(opcion6)
                                   if(opcion6_int>0):
                                       if(opcion6_int<=3):
                                           break
                                   else:
                                       print("ingrese un numero entre 1 y 3")
                               else:
                                   print("ingrese una opcion valida")
                                   pause()
                                   os.system("cls")
                           if(opcion6_int==1):
                               a[i][4]=enfermedades()
                               k=a[i][4]
                               a[i][5]=tratamiento(k)
                               print(a[i])
                               pause()
                               seguro=True
                           if(opcion6_int==2):
                               a.pop(i)
                               print(a)
                               pause()
                               seguro=True
                               break
                           if(opcion6_int==3):
                               seguro=True
                               break
                    if(seguro==True):
                        break
                print("¿Desea volver a buscar una ficha?\ningrese cualquier numero para volver a buscar\ncaso contrario presione 1")
                q="desicion"
                desicion3=validaciondesicion(q)
                if(desicion3==1):
                    return a
                else:
                    w="cedula de identidad:"
                    cedula=w+" "+validacioncedula()
                        
                
                                        
        elif(opcion3_int==2):
            break
            pause()
        else:
            print("ingrese una de las opciones disponibles")
            pause()
        
def ingresoelemento():
    while True:
        while True:
            print("menu\ningrese 1 para ingresar un nuevo prodcuto\ningrese 2 para buscar un prodcuto\ningrese 3 imprimir los productos ingresados\ningrese 4 para volver al menu principal")
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
                        p=input("ingrese el nombre del producto\n")
                    if (s==3):
                        p=listamateriales()
                    if (s==4):
                        q="cantidad de producto que tiene:"
                        p=validacionnumerica2(q)
                    a[i].append(p)
                    s=s+1
                
                print(a)
                pause()
                print("si quiere ingresar otro producto presione cualquier tecla\ncaso contrario presione 1")
                q="desicion"
                desicion=validaciondesicion(q)
                if(desicion==1):
                    break
                s=1
                f=f+1
        elif(opcion4_int==2):
            while True:
                seguro=False
                while True:
                    buscar=input("ingrese el identificador a buscar:")
                    if(buscar.isdigit()==True):
                        buscar_int=int(buscar)
                        if(buscar_int>0):
                            if(buscar_int<=n):
                                break
                        else:
                            print("ingrese un numero mayor a 0")
                    else:
                        print("ingrese un identificador valido")
                        pause()
                        os.system("cls")
                for i in range(len(a)):
                    for j in range(len(a[0])):   
                        if(buscar_int==a[i][j]):
                            print(a[i])
                            while True:
                                print("¿Que desea hacer con este producto?\ningrese 1 para modificar la cantidad del producto\ningrese 2 para eliminar producto")
                                q="desicion"
                                desicion4=validaciondesicion(q)
                                if(desicion4>0):
                                    if(desicion4<=2):
                                        break
                                else:
                                    print("ingrese una de las opciones disponibles")
                                    pause()
                                    os.system("clear")
                            if(desicion4==1):
                                q="cantidad de producto que tiene ahora:"
                                a[i][3]=validacionnumerica2(q)
                                print(a[i])
                                seguro=True
                                break
                            elif(desicion4==2):
                                a.pop(i)
                                print(a)
                                pause()
                                seguro=True
                                break
                    if(seguro==True):
                        break  
                print("¿Desea buscar otro numero?\nsi es asi presione cualquier tecla\n caso contrario presione 1")
                q="desicion"
                desicion5=validaciondesicion(q)
                if(desicion5==1):
                    break
        elif(opcion4_int==3):
            break
        else:
            print("ingrese una de las opciones disponibles")
    return a
def matrizfactura(g):
    acu=0
    m=2
    s=1
    a=[]
    w="cedula de identidad:"
    buscar=w+" "+validacioncedula()
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
            while True:
                v="el valor del procedimiento en centavos"
                b=validacionnumerica2(v)/100
                if(b>0):
                    if(b<1):
                        break
                    else:
                        print("ingrese un numero del 1 al 100")
                else:
                    print("ingrese un numero positivo")
            c="costo:"
            q=z+b
            p=c+str(q)
            acu=acu+q
        a.append(p)
        s=s+1 
    print(a)
    subtotal=acu
    print("el subtotal es:",subtotal)
    IVA=subtotal*0.12
    l=round(IVA,2)
    print("El valor del IVA es:",l)
    total=subtotal+IVA
    d=round(total,2)
    print("el costo total de los procedimientos es:",d)
    pause()

def validacionalfabetica2(nombre):
    while True:
        print("ingrese",nombre,"\n")
        dato=input("ingrese aqui el dato pedido:")
        if(dato.isalpha()==True):
            break
        else:
            print("ingrese un dato valido")
            pause()
            os.system("cls")
    return dato
    
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
def validaciondesicion(nombre):
    while True:
        print("¿cual es su",nombre,"?")
        dato=input("ingrese el dato pedido aqui:")
        if(dato.isdigit()==True):
            dato_int=int(dato)
            if(dato_int>0):
                break
            else:
                print("ingrese un numero mayor a 0")
        else:
            print("ingrese un dato valido")
            pause()
            os.system("cls")
    return dato_int

def validacionnumerica2(nombre):
    while True:
        print("ingrese",nombre,"\n")
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
def listamateriales():
    s=[[1,"higiene dental"],[2,"exodoncia"],[3,"operatoria dental"],[4,"Periodoncia"],[5,"Ortodoncia"],[6,"Material quirurgico"]]
    print("categorias de los productos:\n")
    for i in range(len(s)):
        for j in range(len(s[0])):
            print(s[i][j])
        print("\n")
    while True:
        buscar=input("ingrese un numero entre la lista mostrada:")
        if(buscar.isdigit()==True):
            buscar_int=int(buscar)
            if(buscar_int>0):
                if(buscar_int<=6):
                    break
                else:
                    print("ingrese un numero entre  1 y 6")
                    pause()
            else:
                print("ingrese un numero valido")
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
    print("lista de enfermedades")
    for i in range(len(s)):
        for j in range(len(s[0])):
            print(s[i][j],"\t")
        print("\n")
            
    print("si el diagnostico que busca esta dentro de la lista presione 1\ncaso contrario presione 2 y escriba el diagnostico")
    while True:
        q="desicion"
        desicion5=validaciondesicion(q)
        if(desicion5>0 and desicion5<=2):
            break
        else:
            print("ingrese 1 o 2")
            pause()
    if(desicion5==1):
        while True:
            buscar=input("ingrese un numero entre la lista mostrada:")
            if(buscar.isdigit()==True):
                buscar_int=int(buscar)
                if(buscar_int>0 and buscar_int<=5):
                    break
                else:
                    print("ingrese un numero entre  1 y 5")
                    pause()
            else:
                print("ingrese un numero valido")
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
        dato=input("ingrese el diagnostico:")
    return dato

def tratamiento(enfermedad):
    s=[["caries","empaste en el diente","endodoncia","extraccion del diente"],["gingivitis","limpieza dental","limpieza y restauracion dental"],["periodontitis","raspado","cirugia con colgajos","injerto de tejido blanco","injerto oseo"],["cancer bucal","extirpacion del tumor","diseccion de cuello"],["halitosis","enjuage bucal y dentrificos"]] 
    dato=None
    for i in range(len(s)):
        for j  in range(len(s[0])):
            if(enfermedad==s[i][0]):
                if(s[i][0]=="caries"):
                    while True:
                        print("si las caries son leves ingrese 1\nsi las caries son de gravedad media ingrese 2\nsi son graves ingrese 3")
                        q="su desicion"
                        gravedad=validacionnumerica2(q)
                        if(gravedad<=3):
                            break
                        else:
                            print("ingrese 1, 2 o 3")
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
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                print("ingrese 1 o 2")
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
                        print("si la periodontitis esta en una fase avanzada ingrese 1\ncaso contrario ingrese 2")
                        q="desicion"
                        respuesta=validacionnumerica2(q)
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                print("ingrese 1 o 2")
                                pause()
                                os.system("cls")
                            
                    if(respuesta==1):
                        while True:
                            print("si necesita incisiones minimas ingrese 1\nsi se ha perdido tejido de las encias ingrese 2\nsi el hueso ha sido destruido ingrese 3\n")
                            q="desicion"
                            respuesta2=validacionnumerica2(q)
                            if(respuesta2>0):
                                if(respuesta2<4):
                                    break
                                else:
                                    print("ingrese 1, 2 o 3")
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
                        print("si se extendio al cuello ingrese 1\ncaso contrario ingrese 2")
                        q="desicion"
                        respuesta=validacionnumerica2(q)
                        if(respuesta>0):
                            if(respuesta<=2):
                                break
                            else:
                                print("ingrese si o no")
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
        dato=input("ingrese el tratamiento a realizar:")
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
                    q="un apellido"
                    x=validacionalfabetica(q)
                    w="nombre y apellido:"
                    p=w+g+" "+x #--->esto concantena los strings, esto equivale a los comandos de: strcat(cad0," ");strcat(cad0,cad1);#
                if(s==2):
                    q="una edad"
                    w="edad:"
                    p=w+" "+str(validacionnumerica(q))
                if(s==3):
                    q="un genero"
                    w="genero:"
                    p=w+" "+validacionalfabetica(q)
                if(s==4):
                    w="cedula de identidad:"
                    p=w+" "+validacioncedula()
                if(s==5):
                    w="diagnostico:"
                    x=enfermedades()
                    p=w+" "+x
                z=x
                if(s==6):
                    w="tratamiento:"
                    c=tratamiento(z)
                    p=w+" "+c
                a[i].append(p)
                s=s+1
            print(a)
            pause()
            s=1
            print("si quiere ingresar otra ficha presiones cualquier boton\ncaso contrario presione 1")
            q="desicion"
            desicion=validaciondesicion(q)
            if(desicion==1):
                break
        A=a
        
        while True:
            print("Si desea modificar algo de la matriz presione 1\ncaso contrario presione 2")
            q="desicion"
            desicion8=validaciondesicion(q)
            if(desicion8==1):
                w="cedula de identidad:"
                buscar=w+" "+validacioncedula()
                seguro=False
                for i in range(len(A)):
                    if(buscar==A[i][3]):
                        A=ingresomatrizpacientes(A,buscar)
                        seguro=True
                    if(seguro==True):
                        break
                break
            elif(desicion8==2):
                break
            else:
                print("ingrese una de las opciones disponibles")
    elif (opcion_int==2):
        inventario(opcion_int)
    elif (opcion_int==3):
        facturacion(opcion_int,A)
    elif (opcion_int==4):
        calendario(opcion_int)
        
    elif(opcion_int==5):
        break
    else:
        print("ingrese una de las  opciones disponibles")
        pause()

