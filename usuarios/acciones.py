from usuarios import usuario as modelo
import notas.acciones

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
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nIngresa al sistema: ")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}.")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login Incorrecto, intentalo mas tarde.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (Crear)
        - Mostrar tus notas (Mostrar)
        - Eliminar nota (Eliminar)
        - Salir (Salir)
        """)

        accion = input("Solicite la accion a realizar: ")
        hazEl = notas.acciones.Acciones()

        if accion == "Crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "Mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)
        
        elif accion == "Eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "Salir":
            print(f"Hasta pronto {usuario[1]}.")
            exit()