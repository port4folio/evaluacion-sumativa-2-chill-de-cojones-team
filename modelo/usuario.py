class Usuario:
  def __init__(self, email, password, empleado):
    self.__id = 0
    self.__email = email
    self.__password = password
    self.__empleado = empleado

  def getId (self):
    return self.__id
  
  def getEmpleado (self):
    return self.__empleado
    
  def getEmail (self):
    return self.__email

  def getPassword (self):
    return self.__password
  
  def setId (self, id):
    self.__id = id
  
  def setEmail (self, email):
    self.__email = email  

  def setPassword (self, password):
    self.__password = password  

  def __str__(self):
    return f"{self.__empleado}\n"