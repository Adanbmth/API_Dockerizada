class Carrera():
    def __init__(self,clavecarrera,nombrecarrera=None,estructuragenetica=None) -> None:
        self.clavecarrera = clavecarrera
        self.nombrecarrera = nombrecarrera
        self.estructuragenetica = estructuragenetica

    def to_JSON(self):
        return{
            'Clave': self.clavecarrera,
            'Nombre': self.nombrecarrera,
            'Estructura Genetica': self.estructuragenetica
        }