from usuarios import usuario as modelo

class Acciones:

    def registro(self):
        print("\nTe registraremos en el sistema.")

        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("Ingresa al sistema: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")