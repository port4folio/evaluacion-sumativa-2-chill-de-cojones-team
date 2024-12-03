from modelo.empleado import Empleado
from controlador.controlador_empleado import registrarEmpleado, encontrarEmpleado, actualizarEmpleado, obtenerEmpleados, deleteEmpleado
from controlador.controlador_departamento import obtenerDepartamentos
from vista.vista_departamento import buscarDepartamento

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

def agregarEmpleado():
  print('Ingrese los datos del empleado')
  nombre = input('Ingrese el nombre: ')
  direccion = input('Ingrese la dirección: ')
  telefono = input('Ingrese el teléfono: ')
  email = input('Ingrese el correo electrónico: ')
  fecha_inicio_contrato = input('Ingrese la fecha de inicio de contrato: ')
  salario = int(input('Ingrese el salario: '))
  departamento = buscarDepartamento()
  if departamento is not None:
    empleado = Empleado(nombre, direccion, telefono, email, fecha_inicio_contrato, salario, departamento.getId())
    registrarEmpleado(empleado)
  else:
      print('Departamento no encontrado')

def buscarEmpleado():
  nombre = input('Ingrese el nombre del empleado: ')
  empleado = encontrarEmpleado(nombre)
  return empleado

def editarEmpleado():
  empleado = buscarEmpleado()

  if empleado is not None:
    print('Menu editar empleado')
    print('1.- Nombre')  
    print('2.- Dirección')  
    print('3.- Teléfono')  
    print('4.- Correo eléctronico')  
    print('5.- Salario') 
    print('6.- Reasignar departamento')
    print('0.- Salir')
    op = int(input('Seleccione una opción: '))
    if op == 1:
      print(f'El nombre actual es: {empleado.getNombre()}')
      nombre = input('Ingrese el nuevo nombre: ')
      empleado.setNombre(nombre)
    elif op == 2:
      print(f'La dirección actual es: {empleado.getDireccion()}')
      direccion = input('Ingrese la nueva dirección: ')
      empleado.setDireccion(direccion)
    elif op == 3:
      print(f'El teléfono actual es: {empleado.getTelefono()}')
      telefono = input('Ingrese el nuevo teléfono: ')
      empleado.setTelefono(telefono)
    elif op == 4:
      print(f'El correo eléctronico actual es: {empleado.getEmail()}')
      email = input('Ingrese el nuevo correo eléctronico: ')
      empleado.setEmail(email)
    elif op == 5:
      print(f'El salario actual es: {empleado.getSalario()}')
      salario = int(input('Ingrese el nuevo salario: '))
      empleado.setSalario(salario)
    elif op == 6:
      departamentos = obtenerDepartamentos()
      for depto in departamentos:
        if depto.getId() == empleado.getDepartamento():
          departamento = depto.getNombre()
      print(f'El departamento actual es: {departamento}')
      buscar_departamento = buscarDepartamento()
      if buscar_departamento is not None:
        nuevo_depto = buscar_departamento.getId()
        empleado.setDepartamento(int(nuevo_depto))
        print('Empleado actualizado')
      else:
        print('Departamento no encontrado')
    else:
      print('No se realizaron cambios')
    actualizarEmpleado(empleado)
  else:
    print('Empleado no encontrado')

def imprimirEmpleado():
  empleado = buscarEmpleado()
  if empleado is not None:
    print(empleado)
  else:
    print('Empleado no encontrado')

def imprimirEmpleados():
  empleados = obtenerEmpleados()
  if len(empleados) > 0:
    for empleado in empleados:
      print(empleado)
  else:
    print('No hay empleados ingresados')

def eliminarEmpleado():
  empleado = buscarEmpleado()
  if empleado is not None:
    print(f'Eliminará  el empleado {empleado.getNombre()}')
    print('¿Estás seguro?')
    print('1.- Si')
    print('2.- No')
    print('0.- Salir')
    resp = int(input('Seleccione una opción: '))
    if resp == 1:
      deleteEmpleado(empleado)
    else:
      print('Empleado no eliminado')
  else:
    print('Empleado no encontrado')   
    
def mainEmpleado():
  op = -1
  while op != 0:
    op = menuEmpleado()
    if op == 1:
      agregarEmpleado()
    elif op == 2:
      editarEmpleado()
    elif op == 3:
      imprimirEmpleado()
    elif op == 4:
      imprimirEmpleados()
    elif op == 5:
      eliminarEmpleado()
    