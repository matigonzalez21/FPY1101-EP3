libros = []
titulos = []

def registrar_libro():
    
   
    nombre_libro = input("Ingrese nombre del libro")
    autor = input("Ingrese autor del libro")
    año = int(input("Ingrese año de publicacion"))
    sku = input("Ingrese SKU: SKU es las 6 primeras letras del título del libro , las 3 primeras letras del autor , año de publicación.")
    
    
    libro = {
            "Titulo":nombre_libro,
            "Autor": autor,
            "Año":año,
            "SKU":sku
        }
    libros.append(libro)    
    titulos.append(nombre_libro)

usuarios = []
def prestar_libro():
    try:
        usuario = input("Ingrese su nombre de usuario: ")
        libro_prestado = input("Ingrese el sku del libro requerido: ")
        print ("Se encuentra disponible")
        usuarios.append(usuario)
    except ValueError:
        print ("Datos Incorrectos, Vuelva a colocarlos")


def listar_libros():
    print ("Titulo: \n Autor: \n Año de publicacion: \n SKU: ")
    
    for i in libros:
        print (libros)

fecha_prestamo = "2024"

def imprimir_prestamo():
    
    with open ('imprimir_prestamo.txt', 'w' ) as file:
        for n in libros:
            file.write(f"Usuario: {usuarios} \n Titulo: {titulos} \n Fecha del prestamo:{fecha_prestamo}")
            print("Archivo creado")

while True:
    opcion = int(input("Ingresar opcion:\n 1.Registrar libro\n 2.Prestar libro\n 3.Listar todos los libros\n 4.Imprimir reporte de prestamos\n 5.Salir del programa"))
    if opcion == 1 :
        registrar_libro()        
    elif opcion == 2:
         prestar_libro()
    elif opcion == 3:
         listar_libros()
    elif opcion == 4:
         imprimir_prestamo()
    elif opcion == 5:
        print ("Programa finalizado.....\n Desarrollado por Matias Gonzalez\n Rut:21.742.845-9")
        break

    

