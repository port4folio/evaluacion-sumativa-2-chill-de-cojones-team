from modelo.db import conectar
from modelo.proyecto import Proyecto

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

def proyectosDelEmpleado(empleado):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'SELECT proyecto.id, proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin FROM empleado_proyecto INNER JOIN proyecto ON empleado_proyecto.id_proyecto = proyecto.id WHERE empleado_proyecto.id_empleado = %s',
        (empleado.getId(),)
      )
      proyectos_encontrados = cursor.fetchall()
      proyectos = []
      if len(proyectos_encontrados) > 0:
        for proyecto in proyectos_encontrados:
          proyecto_encontrado = Proyecto(proyecto[1], proyecto[2], proyecto[3], proyecto[4])
          proyecto_encontrado.setId(proyecto[0])
          proyectos.append(proyecto_encontrado)
        return proyectos
      else:
        return None
    else:
      return None
  except Exception as e:
    print(f'Error al conectar {e}')
  finally:
    cursor.close()
    conn.close()