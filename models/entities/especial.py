class Especial():
    def __init__(self,claveespecial,nombremateria=None,creditos=None,semestre=None,claveespecialidad=None) -> None:
        self.claveespecial = claveespecial
        self.nombremateria = nombremateria
        self.creditos = creditos
        self.semestre = semestre
        self.claveespecialidad = claveespecialidad

    def to_JSON(self):
        return{
            'Clave': self.claveespecial,
            'Materia': self.nombremateria,
            'Creditos': self.creditos,
            'Semestre': self.semestre,
            'Especialidad': self.claveespecialidad
        }