class Persona:
  def __init__(self, nombre, direccion, telefono, email):
    self.__id = 0
    self.__nombre = nombre
    self.__direccion = direccion
    self.__telefono = telefono
    self.__email = email

  def getId(self):
    return self.__id

  def getNombre(self):
    return self.__nombre

  def getDireccion(self):
    return self.__direccion
  
  def getTelefono(self):
    return self.__telefono
  
  def getEmail(self):
    return self.__email
  
  def setId(self, id):
    self.__id = id

  def setNombre(self, nombre):
    self.__nombre = nombre

  def setDireccion(self, direccion):
    self.__direccion = direccion

  def setTelefono(self, telefono):
    self.__telefono = telefono

  def setEmail(self, email):
    self.__email = email

  def __str__(self):
    return f"Nombre: {self.__nombre}\nDirección: {self.__direccion}\nNúmero de teléfono: {self.__telefono}\nCorreo electrónico: {self.__email}"