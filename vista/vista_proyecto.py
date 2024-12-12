from modelo.proyecto import Proyecto
from controlador.controlador_proyecto import registrarProyecto, encontrarProyecto, actualizarProyecto, obtenerProyectos, deleteProyecto

def menuProyecto():
  print('Menu Proyecto')
  print("1.- Agregar")
  print("2.- Editar")
  print("3.- Imprimir una")
  print("4.- Eliminar")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def agregarProyecto():
  print('Ingrese los datos del proyecto')
  nombre = input('Ingrese el nombre: ')
  descripcion = input('Ingrese la descripción: ')
  fecha_inicio = input('Ingrese la fecha de inicio del proyecto: ')
  fecha_fin = input('Ingrese la fecha de fin del proyecto: ')
  proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_fin)
  registrarProyecto(proyecto)

def buscarProyecto():
  nombre = input('Ingrese el nombre del proyecto: ')
  proyecto = encontrarProyecto(nombre)
  return proyecto

def editarProyecto():
  proyecto = buscarProyecto()
  if proyecto is not None:
    print('Menu editar proyecto')
    print('1.- Nombre') 
    print('2.- Descripción')
    print('3.- Fecha de inicio del proyecto')
    print('4.- Fecha de fin del proyecto')
    print('0.- Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
      print(f'El nombre actual es: {proyecto.getNombre()}')
      nombre = input('Ingrese el nuevo nombre: ')
      proyecto.setNombre(nombre)
    elif op == 2:
      print(f'La descripcion actual es: {proyecto.getDescripcion()}')
      descripcion = input('Ingrese la nueva descripción: ')
      proyecto.setDescripcion(descripcion)
    elif op == 3:
      print(f'La fecha de inicio actual es: {proyecto.getFechaInicio()}')
      fecha_inicio = input('Ingrese la nueva fecha de inicio: ')
      proyecto.setFechaInicio(fecha_inicio)
    elif op == 4:
      print(f'La fecha de fin actual es: {proyecto.getFechaFin()}')
      fecha_fin = input('Ingrese la nueva fecha de fin: ')
      proyecto.setFechaFin(fecha_fin)
    else:
      print('No se realizaron cambios')
    actualizarProyecto(proyecto)
  else:
    print('Proyecto no encontrado')

def imprimirProyecto():
  proyecto = buscarProyecto()
  if proyecto is not None:
    print(proyecto)
  else:
    print('Proyecto no encontrado')

def eliminarProyecto():
  proyecto = buscarProyecto()
  if proyecto is not None:
    print(f'Eliminará  el proyecto {proyecto.getNombre()}')
    print('¿Estás seguro?')
    print('1.- Si')
    print('2.- No')
    print('0.- Salir')
    resp = int(input('Seleccione una opción: '))
    if resp == 1:
      deleteProyecto(proyecto)
    else:
      print('Proyecto no eliminado')
  else:
    print('Proyecto no encontrado')  

def mainProyecto():
  op = -1
  while op != 0:
    op = menuProyecto()
    if op == 1:
      agregarProyecto()
    elif op == 2:
      editarProyecto()
    elif op == 3:
      imprimirProyecto()
    elif op == 4:
      eliminarProyecto()