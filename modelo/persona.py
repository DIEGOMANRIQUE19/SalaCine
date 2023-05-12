class Persona():
    
    def __init__(self,identificacion=str,nombre=str,correo=str,genero=str):
        """_summary_

        Args:
            identificacion (_str):# documento identidad
            nombre (str): nombre completo de la persona.
            correo (str: correo electrónico de la persona.
            genero (str): Femenino o Mascumino.
        """
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo=correo
        self.__genero=genero
        
    def getIdentificacion(self):
        return self.__identificacion
    
    def getNombre(self):
        return self.__nombre
    
    def getCorreo(self):
        return self.__correo
    
    def getGenero(self):
        return self.__genero
        