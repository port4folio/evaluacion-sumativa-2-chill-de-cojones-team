from vista.vista_empleado import mainEmpleado
from vista.vista_departamento import mainDepartamento
from vista.vista_proyecto import mainProyecto
from vista.vista_empleado_proyecto import mainEmpleadoProyecto
from vista.vista_registro_tiempo import mainRegistrarTiempo
from vista.vista_informe import mainInforme
from controlador.controlador_empleado import obtenerEmpleados
from controlador.controlador_usuario import agregar_usuario, rolUsuario
from modelo.usuario import Usuario

def menuUsuario(usuario):
    rol_depto = rolUsuario(usuario)
    rol, depto = rol_depto if rol_depto else (None, None)
    print('Menu General')
    if rol == 'admin' and depto == 'Recursos Humanos':
      print("1.- Empleado")
      print("0.- Cerrar Sesión")
    elif rol == 'empleado':
      print("1.- Registrar Tiempo")
      print("0.- Cerrar Sesión")
    elif rol == 'admin':
      print("1.- Departamento")
      print("2.- Proyecto")
      print("3.- Empleado a Proyecto")
      print("4.- Generar Informe")
      print("0.- Cerrar Sesión")
    else:
      print("No tiene permisos para acceder a este menú.")
    
    op = int(input("Seleccione una opción: "))
    return op

def registrarUsuario():
  empleados = obtenerEmpleados()
  email = input("Ingrese correo: ")
  password = input("Ingrese contraseña: ")
  empleado_encontrado = False  # Variable de bandera

  if len(empleados) > 0:
    for empleado in empleados:
      if email == empleado.getEmail():
        usuario = Usuario(email, password, empleado)
        agregar_usuario(usuario)
        empleado_encontrado = True
        break  
    if not empleado_encontrado:
      print('No hay ningún empleado registrado con ese correo')
  else:
    print('No hay empleados ingresados')


def mainUsuario(usuario):
  op = -1
  while op != 0:
    op = menuUsuario(usuario)
    if op == 1:
      if rolUsuario(usuario)[0] == 'admin' and rolUsuario(usuario)[1] == 'Recursos Humanos':
        mainEmpleado()
      elif rolUsuario(usuario)[0] == 'empleado':
        mainRegistrarTiempo()
      elif rolUsuario(usuario)[0] == 'admin':
        mainDepartamento()
    elif op == 1 and rolUsuario(usuario)[0] == 'admin':
      mainDepartamento()
    elif op == 2 and rolUsuario(usuario)[0] == 'admin':
      mainProyecto()
    elif op == 3 and rolUsuario(usuario)[0] == 'admin':
      mainEmpleadoProyecto()
    elif op == 4 and rolUsuario(usuario)[0] == 'admin':
      mainInforme()
    elif op == 1 and rolUsuario(usuario)[0] == 'empleado':
      mainRegistrarTiempo()