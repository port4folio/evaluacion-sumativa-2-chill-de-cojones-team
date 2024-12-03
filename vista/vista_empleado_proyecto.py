def menuEmpleado():
  print('Menu Empleado')
  print("1.- Asignar empleado a un proyecto")
  print("2.- Desasignar empleado de un proyecto")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def asignarEmpleado():
  pass

def desasignarEmpleado():
  pass

def mainEmpleadoProyecto():
  op = -1
  while op != 0:
    op = menuEmpleado()
    if op == 1:
      asignarEmpleado()
    elif op == 2:
      desasignarEmpleado()

