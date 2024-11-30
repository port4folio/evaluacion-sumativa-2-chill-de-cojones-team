from modelo.empleado import Empleado
from controlador.controlador_empleado import agregar_empleado

def menuEmpleado():
  print('Menu Empleado')
  print("1.- Agregar")
  print("2.- Editar")
  print("3.- Imprimir una")
  print("4.- Imprimir todas")
  print("5.- Eliminar")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def instanciarEmpleado():
  print('Ingrese los datos del empleado')
  nombre = input('Ingrese el nombre: ')
  direccion = input('Ingrese la dirección: ')
  telefono = input('Ingrese el teléfono: ')
  email = input('Ingrese el correo electrónico: ')
  fecha_inicio_contrato = input('Ingrese la fecha de inicio de contrato: ')
  salario = int(input('Ingrese el salario: '))
  empleado = Empleado(nombre, direccion, telefono, email, fecha_inicio_contrato, salario)
  agregar_empleado(empleado)

def mainEmpleado():
  op = -1
  while op != 0:
    op = menuEmpleado()
    if op == 1:
      instanciarEmpleado()