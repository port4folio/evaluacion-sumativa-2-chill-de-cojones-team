class Departamento:
  def __init__(self, nombre, gerente):
    self.__id = id
    self.__nombre = nombre
    self.__gerente = gerente

  def getId(self):
    return self.__id
  
  def getNombre(self):
    return self.__nombre
  
  def getGerente(self):
    return self.__gerente
  
  def setId(self, id):
    self.__id = id

  def setNombre(self, nombre):
    self.__nombre = nombre

  def setGerente(self, gerente):
    self.__gerente = gerente

  def __str__(self):
    return f'Id: {self.__id}\nNombre: {self.__nombre}\nGerente: {self.__gerente}'