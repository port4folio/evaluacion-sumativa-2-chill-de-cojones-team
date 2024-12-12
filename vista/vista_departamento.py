from modelo.departamento import Departamento
from controlador.controlador_departamento import registrarDepartamento, encontrarDepartamento, actualizarDepartamento, obtenerDepartamentos, deleteDepartamento

def menuDepartamento():
  print('Menu Departamento')
  print("1.- Agregar")
  print("2.- Editar")
  print("3.- Imprimir una")
  print("4.- Eliminar")
  print("0.- Salir")
  op = int(input("Ingrese una opción: "))
  return op

def agregarDepartamento():
  print('Ingrese los datos del departamento')
  nombre = input('Ingrese el nombre: ')
  gerente = input('Ingrese el gerente: ')
  departamento = Departamento(nombre, gerente)
  registrarDepartamento(departamento)

def buscarDepartamento():
  nombre = input('Ingrese el nombre del departamento: ')
  departamento = encontrarDepartamento(nombre)
  return departamento

def editarDepartamento():
  departamento = buscarDepartamento()
  if departamento is not None:
    print('Menu editar departamento')
    print('1.- Nombre') 
    print('2.- Gerente')
    print('0.- Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
      print(f'El nombre actual es: {departamento.getNombre()}')
      nombre = input('Ingrese el nuevo nombre: ')
      departamento.setNombre(nombre)
    elif op == 2:
      print(f'El gerente actual es: {departamento.getGerente()}')
      gerente = input('Ingrese el nuevo gerente: ')
      departamento.setGerente(gerente)
    else:
      print('No se realizaron cambios')
    actualizarDepartamento(departamento)
  else:
    print('Departamento no encontrado')

def imprimirDepartamento():
  departamento = buscarDepartamento()
  if departamento is not None:
    print(departamento)
  else:
    print('Departamento no encontrado')

def eliminarDepartamento():
  departamento = buscarDepartamento()
  if departamento is not None:
    print(f'Eliminará  el departamento {departamento.getNombre()}')
    print('¿Estás seguro?')
    print('1.- Si')
    print('2.- No')
    print('0.- Salir')
    resp = int(input('Seleccione una opción: '))
    if resp == 1:
      deleteDepartamento(departamento)
    else:
      print('Departamento no eliminado')
  else:
    print('Departamento no encontrado')  

def mainDepartamento():
  op = -1
  while op != 0:
    op = menuDepartamento()
    if op == 1:
      agregarDepartamento()
    elif op == 2:
      editarDepartamento()
    elif op == 3:
      imprimirDepartamento()
    elif op == 4:
      eliminarDepartamento()