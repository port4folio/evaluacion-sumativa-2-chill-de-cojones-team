from modelo.db import conectar
from datetime import datetime

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
  