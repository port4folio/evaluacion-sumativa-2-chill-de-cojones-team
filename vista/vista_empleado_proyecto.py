from controlador.controlador_empleado import obtenerEmpleados
from controlador.controlador_proyecto import obtenerProyectos
from controlador.controlador_empleado_proyecto import registrarEmpleadoAProyecto, eliminarEmpleadoDeProyecto

def menuEmpleado():
  print('Menu empleado a proyecto')
  print("1.- Asignar empleado a un proyecto")
  print("2.- Desasignar empleado de un proyecto")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op
  
def seleccionarEmpleado():
  empleados = obtenerEmpleados()
  if len(empleados) > 0:
    print('Seleccione un empleado:')
    for i, empleado in enumerate(empleados):
      print(f'{i + 1}.- {empleado.getNombre()}')
    op = int(input('Seleccione una opción: '))
    if 1 <= op <= len(empleados):
      empleado_seleccionado = empleados[op - 1]
      return empleado_seleccionado
    else:
      print('Opción no válida')
  else:
    print('No hay empleados ingresados')

def seleccionarProyecto():
  proyectos = obtenerProyectos()
  if len(proyectos) > 0:
    print('Seleccione un proyecto:')
    for i, proyecto in enumerate(proyectos):
      print(f'{i + 1}.- {proyecto.getNombre()}')
    op = int(input('Seleccione una opción: '))
    if 1 <= op <= len(proyectos):
      proyecto_seleccionado = proyectos[op - 1]
      return proyecto_seleccionado
    else:
      print('Opción no válida')
  else:
    print('No hay proyectos ingresados')

def asignarEmpleado():
  empleado = seleccionarEmpleado()
  proyecto = seleccionarProyecto()
  print(f'Asignara al empleado {empleado.getNombre()} en el proyecto {proyecto.getNombre()}')
  print('¿Estás seguro?')
  print('1.- Si')
  print('2.- No')
  print('0.- Salir')
  resp = int(input('Seleccione una opción: '))
  if resp == 1:
    registrarEmpleadoAProyecto(empleado, proyecto)
  else:
    print('Empleado no eliminado')
  

def desasignarEmpleado():
  empleado = seleccionarEmpleado()
  proyecto = seleccionarProyecto()
  print(f'Eliminará al empleado {empleado.getNombre()} del proyecto {proyecto.getNombre()}')
  print('¿Estás seguro?')
  print('1.- Si')
  print('2.- No')
  print('0.- Salir')
  resp = int(input('Seleccione una opción: '))
  if resp == 1:
    eliminarEmpleadoDeProyecto(empleado, proyecto)
  else:
    print('Empleado no eliminado')

def mainEmpleadoProyecto():
  op = -1
  while op != 0:
    op = menuEmpleado()
    if op == 1:
      asignarEmpleado()
    elif op == 2:
      desasignarEmpleado()

