from modelo.persona import Persona

class Empleado(Persona):
  def __init__(self, nombre, direccion, telefono, email, rol, fecha_inicio_contrato, salario, departamento):
    super().__init__(nombre, direccion, telefono, email)
    self.__rol = rol
    self.__fecha_inicio_contrato = fecha_inicio_contrato
    self.__salario = salario
    self.__departamento = departamento

  # Obtener atributos
  def getFechaInicioContrato(self):
    return self.__fecha_inicio_contrato

  def getRol(self):
    return self.__rol

  def getSalario(self):
    return self.__salario
  
  def getDepartamento(self):
    return self.__departamento
  
  # Modificar atributos
  def setRol(self, rol):
    self.__rol = rol

  def setFechaInicioContrato(self, fecha_inicio_contrato):
    self.__fecha_inicio_contrato = fecha_inicio_contrato

  def setSalario(self, salario):
    self.__salario = salario

  def setDepartamento(self, departamento):
    self.__departamento = departamento

  def __str__(self):
    return super().__str__() + f'\nRol: {self.__rol}\nFecha de inicio de contrato: {self.__fecha_inicio_contrato}\nSalario: ${self.__salario}'