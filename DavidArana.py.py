registro_libro={}
libros_registrados={}
registro_venta={}
libros_ficcion=[]
libros_romance=[]
libros_miedo=[]

def registro_de_libro():
    orden=int(input("Ingrese el numero del libro, por ejemplo '3' para que sea mas ordenado "))
    autor= input("Ingrese el nombre del autor: ")
    titulo= input("Ingrese el titulo del libro: ")
    genero= input("Ingrese el genero del libro |Ficcion,Miedo,Romance|: ")
    precio= int(input("Ingrese el precio de libro: "))
    libros_registrados["LIBRO NUMERO", orden] = {"Autor": autor, "Titulo": titulo, "Genero": genero, "Precio": precio}
    print("Libro registrado exitosamente!")
    print(orden)
    if genero=="Ficcion":
        genero.append(libros_ficcion)
    elif genero=="Romance":
        genero.append(libros_romance)
    elif genero=="Miedo":
        genero.append(libros_miedo)

def lista_libros():
    print("---Libros registrados---")
    print(libros_registrados)

def registrar_ventas():
    print("---Registro de ventas---")
    titulon= input("Ingrese el titulo del libro: ")
    vendido= int(input("Ingrese cantidad vendida del libro: "))
    registro_venta[titulon] = {"Vendido": vendido}
    if titulon==libros_registrados:
        print("Venta con exito")
    else:
        print("Venta fallida")

def reporte_ventas():
    print("Dese imprimir todos los reportes (1) o por genero? (2)")
    op=int(input("Ingrese opcion 1 o 2: "))
    if op==1:
        print(registro_venta)
    elif op==2:
        print("Elija que genero desea reportar")
        print("1)Ficcion")
        print("2)Romance")
        print("3)Miedo")
        op1=int(input("Elija alguna opcion: "))
        if op1==1:
            print(libros_ficcion)
        elif op1==2:
            print(libros_romance)
        elif op1==3:
            print(libros_miedo)

def generar_txt():
    with open({registro_venta}.txt,"w"):
        json.write(registro_venta)

while True:
    print("---MENU---")
    print("1. Registrar libro")
    print("2. Listar todos los libros")
    print("3. Registrar venta")
    print("4. Imprimir reporte de ventas")
    print("5. Generar txt")
    print("5. Salir")
    res= int(input("Ingrese alguna opcion: "))

    if res==1:
        registro_de_libro()
    elif res==2:
        lista_libros()
    elif res==3:
        registrar_ventas()
    elif res==4:
        reporte_ventas()
    elif res==5:
        generar_txt()
    elif res==6:
        print("Gracias")
        break