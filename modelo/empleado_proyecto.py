class EmpleadoProyecto:
  def __init__(self, empleado, proyecto):
    self.__empleado = empleado
    self.__proyecto = proyecto

  def asignar(self):
    self.empleado.asignar_proyecto(self.__proyecto)
    self.proyecto.asignar_empleado(self.__empleado)

  def desasignar(self):
    self.empleado.desasignar_proyecto(self.__proyecto)
    self.proyecto.desasignar_empleado(self.__empleado)