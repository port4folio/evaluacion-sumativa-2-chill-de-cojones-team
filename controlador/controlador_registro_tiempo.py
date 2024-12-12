from modelo.db import conectar
from datetime import datetime
from modelo.registro_tiempo import RegistroTiempo

def agregarHorasTrabajadas(registro_tiempo):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      fecha = datetime.strptime(registro_tiempo.getFecha(), '%d-%m-%Y').date()
      cursor.execute(
        'INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion) VALUES(%s, %s, %s, %s, %s)',
        (registro_tiempo.getIdEmpleado(), registro_tiempo.getIdProyecto(), fecha, registro_tiempo.getHorasTrabajadas(), registro_tiempo.getDescripcion())
      )
      conn.commit()
      print('Horas trabajadas ingresadas')
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()
  

def obtenerRegistros():
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM registro_tiempo')
      registros_encontrados = cursor.fetchall()
      registros = []
      if len(registros_encontrados) > 0:
        for registro in registros_encontrados:
          registro_encontrado = RegistroTiempo(registro[1], registro[2], registro[3], registro[4], registro[5])
          registro_encontrado.setId(registro[0])
          registros.append(registro_encontrado)
        return registros
      else:
        return None
    else:
      return None
  except Exception as e:
    print(f'Error al conectar {e}')
  finally:
    cursor.close()
    conn.close()