from vista.vista_empleado import mainEmpleado
from vista.vista_departamento import mainDepartamento

def menu():
  print('Menu General')
  print("1.- Empleado")
  print("2.- Departamento")
  print("0.- Salir")
  op = int(input("Seleccione una opción: "))
  return op

while True:
  op = menu()
  if op == 1:
    mainEmpleado()
  elif op == 2:
    mainDepartamento()
  elif op == 0:
    print('Gracias')
    break
  else:
    print("Debe seleccionar una opción válida")
    break