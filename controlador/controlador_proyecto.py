from modelo.db import conectar
from datetime import datetime
from modelo.proyecto import Proyecto

def registrarProyecto(proyecto):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      fecha_inicio_proyecto = datetime.strptime(proyecto.getFechaInicio(), '%d-%m-%Y').date()
      if proyecto.getFechaFin():
        fecha_fin_proyecto = datetime.strptime(proyecto.getFechaFin(), '%d-%m-%Y').date()
      else:
        fecha_fin_proyecto = None
      cursor.execute(
        'INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_fin) VALUES(%s, %s, %s, %s)',
        (proyecto.getNombre(), proyecto.getDescripcion(), fecha_inicio_proyecto, fecha_fin_proyecto)
      )
      conn.commit()
      print('Proyecto ingresado')
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def encontrarProyecto(nombre):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'SELECT * FROM proyecto WHERE nombre = %s',
        (nombre,)
      )
      proyecto = cursor.fetchone()
      if proyecto is not None:
        proyecto_encontrado = Proyecto(proyecto[1], proyecto[2], proyecto[3], proyecto[4])
        proyecto_encontrado.setId(proyecto[0])
      else:
        proyecto_encontrado = None
      return proyecto_encontrado
    else:
      return None
  except Exception as e:
    print(f'No se encontraron registros {e}')
  finally:
    cursor.close()
    conn.close()

def actualizarProyecto(proyecto):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      fecha_inicio_proyecto = proyecto.getFechaInicio()
      if isinstance(fecha_inicio_proyecto, str):
        fecha_inicio_proyecto = datetime.strptime(fecha_inicio_proyecto, '%d-%m-%Y').date()
            
      fecha_fin_proyecto = proyecto.getFechaFin()
      if isinstance(fecha_fin_proyecto, str):
        fecha_fin_proyecto = datetime.strptime(fecha_fin_proyecto, '%d-%m-%Y').date()

      cursor.execute(
        'UPDATE proyecto SET nombre = %s, descripcion = %s, fecha_inicio = %s, fecha_fin = %s WHERE id = %s',
        (proyecto.getNombre(), proyecto.getDescripcion(), fecha_inicio_proyecto, fecha_fin_proyecto, proyecto.getId())
      )
      conn.commit()
      print('Proyecto actualizado')
  except Exception as e:
    print(f'No se actualizaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def obtenerProyectos():
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM proyecto')
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

def deleteProyecto(proyecto):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'DELETE FROM proyecto WHERE id = %s',
        (proyecto.getId(),)
      )
      conn.commit()
      print('Proyecto eliminado')
  except Exception as e:
    print(f'No se eliminaron registros {e}')
  finally:
    cursor.close()
    conn.close()