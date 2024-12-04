from controlador.controlador_autenticacion import autenticar
from vista.vista_usuario import mainUsuario, registrarUsuario

def menu():
  print('Menu General')
  print("1.- Login")
  print("2.- Registrarse")
  print("0.- Salir")
  op = int(input("Seleccione una opción: "))
  return op

while True:
  op = menu()
  if op == 1:
    print("Inicio sesión")
    email=input("Ingrese correo: ")
    password=input("Ingrese contraseña: ")
    usuario = autenticar(email, password)
    if usuario is not None:
      mainUsuario(usuario)
  elif op == 2:
    registrarUsuario()
  elif op == 0:
    print('Gracias')
    break
  else:
    print("Debe seleccionar una opción válida")
    break