from modelo.db import conectar
from modelo.departamento import Departamento

def registrarDepartamento(departamento):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'INSERT INTO departamento (nombre, gerente) VALUES(%s, %s)',
        (departamento.getNombre(), departamento.getGerente())
      )
      conn.commit()
      print('Departamento ingresado')
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def encontrarDepartamento(nombre):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'SELECT * FROM departamento WHERE nombre = %s',
        (nombre,)
      )
      departamento = cursor.fetchone()
      if departamento is not None:
        departamento_encontrado = Departamento(departamento[1], departamento[2])
        departamento_encontrado.setId(departamento[0])
      else:
        departamento_encontrado = None
      return departamento_encontrado
    else:
      return None
  except Exception as e:
    print(f'No se agregaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def actualizarDepartamento(departamento):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'UPDATE departamento SET nombre = %s, gerente = %s WHERE id = %s',
        (departamento.getNombre(), departamento.getGerente(), departamento.getId())
      )
      conn.commit()
      print('Departamento actualizado')
  except Exception as e:
    print(f'No se actualizaron registros {e}')
  finally:
    cursor.close()
    conn.close()

def obtenerDepartamentos():
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM departamento')
      departamentos_encontrados = cursor.fetchall()
      departamentos = []
      if len(departamentos_encontrados) > 0:
        for departamento in departamentos_encontrados:
          departamento_encontrado = Departamento(departamento[1], departamento[2])
          departamento_encontrado.setId(departamento[0])
          departamentos.append(departamento_encontrado)
        return departamentos
      else:
        return None
    else:
      return None
  except Exception as e:
    print(f'Error al conectar {e}')
  finally:
    cursor.close()
    conn.close()

def deleteDepartamento(departamento):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'DELETE FROM departamento WHERE id = %s',
        (departamento.getId(),)
      )
      conn.commit()
      print('Departamento eliminado')
  except Exception as e:
    print(f'No se eliminaron registros {e}')
  finally:
    cursor.close()
    conn.close()