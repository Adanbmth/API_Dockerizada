class Materia():
    def __init__(self,clavemateria,nombremateria=None,creditos=None,semestre=None,clavecarrera=None) -> None:
        self.clavemateria = clavemateria
        self.nombremateria = nombremateria
        self.creditos = creditos
        self.semestre = semestre
        self.clavecarrera = clavecarrera

    def to_JSON(self):
        return{
            'Clave': self.clavemateria,
            'Materia': self.nombremateria,
            'Creditos': self.creditos,
            'Semestre': self.semestre,
            'Carrera': self.clavecarrera
        }