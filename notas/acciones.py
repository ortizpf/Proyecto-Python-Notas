import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}. Vamos a crear una nueva nota.")

        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nHas guartdado la nota: {nota.titulo}")
        else:
            print("\nNo se ha guardado la nota.")

    def mostrar(self, usuario):
        print(f"\nAqui tienes tus notas {usuario[1]}: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        # Recorrer notas para mostrar titulo y descrip.
        for nota in notas:
            print("\n***************************************")
            print(nota[2])
            print(nota[3])

    def borrar(self, usuario):
        print(f"\n{usuario[1]}, estamos dentro de la opcion Eliminar.")

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota: {nota.titulo}")
        else:
            print("No se ha podido eliminar la nota, intentelo mas tarde.")