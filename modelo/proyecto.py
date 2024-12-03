class Proyecto:
  def __init__(self, nombre, descripcion, fecha_inicio, fecha_fin):
    self.__id = id
    self.__nombre = nombre
    self.__descripcion = descripcion
    self.__fecha_inicio = fecha_inicio
    self.__fecha_fin = fecha_fin

  def getId (self):
    return self.__id
    
  def getNombre(self):
    return self.__nombre
    
  def getDescripcion(self):
    return self.__descripcion
  
  def getFechaInicio(self):
    return self.__fecha_inicio
  
  def getFechaFin(self):
    return self.__fecha_fin
  
  def setId(self, id):
    self.__id = id

  def setNombre(self, nombre):
    self.__nombre = nombre

  def setDescripcion(self, descripcion):
    self.__descripcion = descripcion
    
  def setFechaInicio(self, fecha_inicio):
    self.__fecha_inicio = fecha_inicio
    
  def setFechaFin(self, fecha_fin):
    self.__fecha_fin = fecha_fin  
  
  def __str__(self):
    return f'Nombre: {self.__nombre}\nDescripción: {self.__descripcion}\nFecha de inicio: {self.__fecha_inicio}\nFecha fin: {self.__fecha_fin}'
  