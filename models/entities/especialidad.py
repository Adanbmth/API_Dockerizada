class Especialidad():
    def __init__(self,claveespecialidad,nombreespecialidad=None,creditos=None,clavecarrera=None) -> None:
        self.claveespecialidad = claveespecialidad
        self.nombreespecialidad = nombreespecialidad
        self.creditos = creditos
        self.clavecarrera = clavecarrera

    def to_JSON(self):
        return{
            'Clave': self.claveespecialidad,
            'Especialidad': self.nombreespecialidad,
            'Creditos': self.creditos,
            'Carrera': self.clavecarrera
        }