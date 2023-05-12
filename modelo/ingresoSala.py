from modelo.silla import Silla
from modelo.persona import Persona
from datetime import datetime

class IngresoSala():
    
    def __init__(self,persona=Persona,silla=Silla):
        """_summary_
            constructor crear objeto que representa
            el ingreso a la sala
        Args:
            persona (Persona): Objeto de tipo Persona.
            silla (Silla): Objeto de tipo silla.
        """
        self.__persona=persona
        self.__silla=silla
        self.__fechaHora = datetime.now()
        
    def getPersona(self):
        return self.__persona
    
    def getSilla(self):
        return self.__silla
    
    def getFechaHora(self):
        return self.__fechaHora