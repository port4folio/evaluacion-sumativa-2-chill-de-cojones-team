from modelo.db import conectar
import bcrypt

def buscarUsuario(email):
  conn=conectar()
  if conn is not None:
    try:
      cursor=conn.cursor()
      cursor.execute("SELECT * FROM usuario WHERE email=%s",(email,))
      usuario=cursor.fetchone()
      return usuario
    except Exception as e:
      print(e)
    finally:
      cursor.close()
      conn.close()

def agregar_usuario(usuario):
  conn=conectar()
  if conn is not None:
    try:
      cursor=conn.cursor()
      pwd_hash=bcrypt.hashpw(usuario.getPassword().encode('utf-8'),bcrypt.gensalt())
      cursor.execute(
        "INSERT INTO usuario(email, password, id_empleado) VALUES(%s,%s,%s)",
        (usuario.getEmail(), pwd_hash, usuario.getEmpleado().getId())
      )
      conn.commit()
      print("Usuario agregado")
    except Exception as e:
      print(e)
    finally:
      cursor.close()
      conn.close()

def rolUsuario(usuario):
  conn = conectar()
  try:
    if conn is not None:
      cursor = conn.cursor()
      cursor.execute(
        'SELECT empleado.rol, departamento.nombre FROM usuario INNER JOIN empleado ON usuario.id_empleado = empleado.id INNER JOIN departamento ON empleado.id_departamento = departamento.id WHERE usuario.id = %s;',
        (usuario[0],)
      )
      resultado = cursor.fetchone()
      if resultado:
        return resultado  # Retorna una tupla (rol, nombre_departamento)
      else:
        return None  # Si no se encuentra el usuario
  except Exception as e:
    print(f"Error: {e}")
  finally:
    if conn:
      conn.close()
      
"""         return proyectos
      else:
        return None
    else:
      return None
  except Exception as e:
    print(f'Error al conectar {e}')
  finally:
    cursor.close()
    conn.close() """