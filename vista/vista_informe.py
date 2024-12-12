from controlador.controlador_empleado import obtenerEmpleados
from controlador.controlador_departamento import obtenerDepartamentos
from controlador.controlador_proyecto import obtenerProyectos
from controlador.controlador_registro_tiempo import obtenerRegistros

def menuInforme():
  print('Menu Informe')
  print("1.- Generar informe de empleados")
  print("2.- Generar informe de departamento")
  print("3.- Generar informe de proyecto")
  print("4.- Generar informe de registro de tiempos")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def imformeEmpleado():
  empleados = obtenerEmpleados()
  if len(empleados) > 0:
    for empleado in empleados:
      print(empleado)
  else:
    print('No hay empleados para generar informes')

def informeDepartamento():
  departamentos = obtenerDepartamentos()
  if len(departamentos) > 0:
    for departamento in departamentos:
      print(departamento)
  else:
    print('No hay departamentos para generar informes')

def informeProyecto():
  proyectos = obtenerProyectos()
  if len(proyectos) > 0:
    for proyecto in proyectos:
      print(proyecto)
  else:
    print('No hay proyectos para generar el informe')

def informeRegistroTiempo():
  registros = obtenerRegistros()
  if len(registros) > 0:
    for registro in registros:
      print(registro)
  else:
    print('No hay registros de tiempo para generar el informe')

def mainInforme():
  op = -1
  while op != 0:
    op = menuInforme()
    if op == 1:
      imformeEmpleado()
    elif op == 2:
      informeDepartamento()
    elif op == 3:
      informeProyecto()
    elif op == 4:
      informeRegistroTiempo()