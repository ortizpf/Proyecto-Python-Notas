"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la BD
- Si elegimos login, identificara al usuario y nos preguntara:
    - Crear nota, mostrar notas, borrarlas.
"""

print("""
Acciones disponibles:
      - Registro
      - Login
""")

accion = input("Solicite una de las 2 acciones disponibles: ")

if accion == "Registro":
    print("Te registraremos en el sistema.")

elif accion == "Login":
    print("Introduce tu email y contraseña: ")