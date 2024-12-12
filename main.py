from controlador.controlador_autenticacion import autenticar
from vista.vista_usuario import mainUsuario, registrarUsuario
from vista.vista_indicadores import main_indicadores

def menu():
  print('Menu General')
  print("1.- Login")
  print("2.- Registrarse")
  print("3.- Indicadores")
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
  elif op == 3:
    main_indicadores()
  elif op == 0:
    print('Gracias')
    break
  else:
    print("Debe seleccionar una opción válida")
    break