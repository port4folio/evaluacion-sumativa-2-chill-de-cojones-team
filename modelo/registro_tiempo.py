class RegistroTiempo:
  def __init__(self, id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion):
    self.__id = 0
    self.__id_empleado = id_empleado
    self.__id_proyecto = id_proyecto
    self.__fecha = fecha
    self.__horas_trabajadas = horas_trabajadas
    self.__descripcion = descripcion

  def getId(self):
    return self.__id

  def getIdEmpleado(self):
    return self.__id_empleado
  
  def getIdProyecto(self):
    return self.__id_proyecto
  
  def getFecha(self):
    return self.__fecha
  
  def getHorasTrabajadas(self):
    return self.__horas_trabajadas
  
  def getDescripcion(self):
    return self.__descripcion
  
  # Modificar atributos
  def setId(self, id):
    self.__id = id

  def setIdEmpleado(self, id_empleado):
    self.__id_empleado = id_empleado

  def setIdProyecto(self, id_proyecto):
    self.__id_proyecto = id_proyecto

  def setFecha(self, fecha):
    self.__fecha = fecha

  def setHorasTrabajadas(self, horas_trabajadas):
    self.__horas_trabajadas = horas_trabajadas

  def setDescripcion(self, descripcion):
    self.__descripcion = descripcion

  def __str__(self):
    return f"Empleado: {self.__id_empleado}\nProyecto: {self.__id_proyecto}\nFecha: {self.__fecha}\nHoras Trabajadas: {self.__horas_trabajadas}\nDescripción: {self.__descripcion}"