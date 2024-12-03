from vista.vista_empleado import buscarEmpleado
from controlador.controlador_empleado_proyecto import proyectosDelEmpleado
from controlador.controlador_registro_tiempo import agregarHorasTrabajadas
from modelo.registro_tiempo import RegistroTiempo
from datetime import timedelta

def validarTiempo(tiempo):
  if 0 < tiempo <= 12:
      return True
  else:
    print("Las horas trabajadas deben estar entre 1 y 12.")
    return False
  
def convertir_horas_a_time(horas_decimal):
  horas = int(horas_decimal)
  minutos = int((horas_decimal - horas) * 60)
  return timedelta(hours=horas, minutes=minutos)

def menuRegistrarTiempo():
  fecha = input('Ingrese la fecha que trabajó en el proyecto: ')
  horas_trabajadas = float(input('Ingrese las horas trabajadas (en formato decimal, por ejemplo, 8.5): '))
  if validarTiempo(horas_trabajadas):
    horas_time = convertir_horas_a_time(horas_trabajadas)
    descripcion = input('Ingrese la descripción del trabajo que realizó: ')
  
  return [fecha, horas_time, descripcion]


def mainRegistrarTiempo():
  empleado = buscarEmpleado()
  if empleado is not None:
    proyectos = proyectosDelEmpleado(empleado)
    if proyectos:
      print(f'El empleado {empleado.getNombre()} está en los siguientes proyectos')
      print(f'Selecciona el proyecto para registrar las horas trabajadas: ')
      for i, proyecto in enumerate(proyectos):
        print(f'{i + 1}.- {proyecto.getNombre()}')
      op = int(input('Seleccione una opción: '))
      if 1 <= op <= len(proyectos):
        proyecto_seleccionado = proyectos[op - 1]
        datos = menuRegistrarTiempo()
        registro_tiempo = RegistroTiempo(empleado.getId(), proyecto_seleccionado.getId(), datos[0], datos[1], datos[2])
        agregarHorasTrabajadas(registro_tiempo)
      else:
        print('Opción no válida')
    else:
      print(f'El empleado {empleado.getNombre()} no está en ningún proyecto.')
  else:
    print('Empleado no encontrado') 