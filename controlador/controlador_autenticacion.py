from controlador.controlador_usuario import buscarUsuario
import bcrypt

def autenticar(email, password):
  usuario = buscarUsuario(email)
  if usuario is not None:
    if bcrypt.checkpw(password.encode('utf-8'), usuario[2].encode('utf-8')):
      return usuario
  return None