from modelo.db import conectar

def registrarEmpleadoAProyecto(empleado, proyecto):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES(%s, %s)',
        (empleado.getId(), proyecto.getId())
      )
      conn.commit()
      print(f'Empleado {empleado.getNombre()} ingresado a proyecto {proyecto.getNombre()}')
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def eliminarEmpleadoDeProyecto(empleado, proyecto):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'DELETE FROM empleado_proyecto WHERE id_empleado = %s AND id_proyecto = %s',
        (empleado.getId(), proyecto.getId())
      )
      conn.commit()
      print(f'Empleado {empleado.getNombre()} eliminado del proyecto {proyecto.getNombre()}')
  except Exception as e:
    print(f'No se eliminaron registros {e}')
  finally:
    cursor.close()
    conn.close()