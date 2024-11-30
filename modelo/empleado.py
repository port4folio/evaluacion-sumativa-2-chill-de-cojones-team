class Empleado:
  def __init__(self, nombre, direccion, telefono, email, fecha_inicio_contrato, salario):
    self.__nombre = nombre
    self.__direccion = direccion
    self.__telefono = telefono
    self.__email = email
    self.__fecha_inicio_contrato = fecha_inicio_contrato
    self.__salario = salario

  # Obtener atributos
  def getNombre(self):
    return self.__nombre
  
  def getDireccion(self):
    return self.__direccion
  
  def getTelefono(self):
    return self.__telefono
  
  def getEmail(self):
    return self.__email
  
  def getFechaInicioContrato(self):
    return self.__fecha_inicio_contrato

  def getSalario(self):
    return self.__salario
  
  # Modificar atributos
  def setNombre(self, nombre):
    self.__nombre = nombre

  def setTelefono(self, telefono):
    self.__telefono = telefono

  def setEmail(self, email):
    self.__email = email

  def setFechaInicioContrato(self, fecha_inicio_contrato):
    self.__fecha_inicio_contrato = fecha_inicio_contrato

  def setSalario(self, salario):
    self.__salario = salario

  def __str__(self):
    return f'Nombre: {self.__nombre}\nNúmero de teléfono: {self.__telefono}\nCorreo electrónico: {self.__email}\nFecha de inicio de contrato: {self.__fecha_inicio_contrato}\nSalario: {self.__salario}'