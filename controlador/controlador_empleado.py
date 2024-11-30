from modelo.db import conectar
from datetime import datetime

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