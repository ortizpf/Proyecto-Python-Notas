"""
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la BD
- Si elegimos login, identificara al usuario y nos preguntara:
    - Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
      - Registro
      - Login
""")

hazEl = acciones.Acciones()     # Instanciando mi clase

accion = input("Solicite una de las 2 acciones disponibles: ")

if accion == "Registro":
    hazEl.registro()

elif accion == "Login":
    hazEl.login()

