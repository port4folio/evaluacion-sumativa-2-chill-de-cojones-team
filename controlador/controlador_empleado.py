from modelo.db import conectar
from datetime import datetime
from modelo.empleado import Empleado

def agregar_empleado(empleado):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      fecha_inicio_contrato = datetime.strptime(empleado.getFechaInicioContrato(), '%d-%m-%Y').date()
      cursor.execute(
        'INSERT INTO empleado (nombre, direccion, telefono, email, fecha_inicio_contrato, salario) VALUES(%s, %s, %s, %s, %s, %s)',
        (empleado.getNombre(), empleado.getDireccion(), empleado.getTelefono(), empleado.getEmail(), fecha_inicio_contrato, empleado.getSalario())
      )
      conn.commit()
      print('Empleado ingresado')
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def encontrarEmpleado(nombre):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'SELECT * FROM empleado WHERE nombre = %s',
        (nombre,)
      )
      empleado = cursor.fetchone()
      if empleado is not None:
        empleado_encontrado = Empleado(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6])
        empleado_encontrado.setId(empleado[0])
      else:
        empleado_encontrado = None
      return empleado_encontrado
    else:
      return None
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def actualizarEmpleado(empleado):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'UPDATE empleado SET nombre = %s, direccion = %s, telefono = %s, email = %s, salario = %s WHERE id = %s',
        (empleado.getNombre(), empleado.getDireccion(), empleado.getTelefono(), empleado.getEmail(), empleado.getSalario(), empleado.getId())
      )
      conn.commit()
      print('Empleado actualizado')
  except Exception as e:
    print(f'No se actualizaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def obtenerEmpleados():
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM empleado')
      empleados_encontrados = cursor.fetchall()
      empleados = []
      if len(empleados_encontrados) > 0:
        for empleado in empleados_encontrados:
          empleado_encontrado = Empleado(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6])
          empleado_encontrado.setId(empleado[0])
          empleados.append(empleado_encontrado)
        return empleados
      else:
        return None
    else:
      return None
  except Exception as e:
    print(f'Error al conectar {e}')
  finally:
    cursor.close()
    conn.close()

def deleteEmpleado(empleado):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'DELETE FROM empleado WHERE id = %s',
        (empleado.getId(),)
      )
      conn.commit()
      print('Empleado eliminado')
  except Exception as e:
    print(f'No se eliminaron registros {e}')
  finally:
    cursor.close()
    conn.close()