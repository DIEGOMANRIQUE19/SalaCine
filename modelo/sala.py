from modelo.silla import Silla
from modelo.persona import Persona
from modelo.ingresoSala import IngresoSala

class Sala():
    
    def __init__(self,nombre=str,cantidadSillas=int):
        self.__nombre=nombre
        self.__cantidadSillas=cantidadSillas
        self.__estado="DISPONIBLE"
        self.__listaSillas=[]
        self.__listaIngresos=[]
        self.__inicializarSillas()
        
    def __inicializarSillas(self):
        for i in range(self.__cantidadSillas):
            silla = Silla(i+1)
            self.__listaSillas.append(silla)
            
    def registrarIngreso(self,identificacion=str, nombre=str,correo=str,genero=str):
        persona = Persona(identificacion,nombre,correo,genero)
        sillaDisponible  = self.__obtenerSillaDisponible()
        if(sillaDisponible is not None):
            ingresoSala = IngresoSala(persona,sillaDisponible)
            self.__listaIngresos.append(ingresoSala)
            sillaDisponible.setPersona(persona)
            sillaDisponible.setEstado()
            return True, "Se ha realizado el registro de ingreso"
        else:
            return False, "No hay silla Disponible"
        
    def __obtenerSillaDisponible(self):
        for silla in self.__listaSillas:
            if  silla.getEstado()=="DISPONIBLE":
                return silla 
        
        return None
    
    def obtenerDatosPersonaSilla(self, numero=int):
        for silla in self.__listaSillas:
            if silla.getNumero()==numero:
                if(silla.getEstado()=="OCUPADO"):
                    return silla.getPersona()
                else:
                    return "No hay persona sentada en esa silla"
            
        return "No existe silla con ese número"
    
    def obtenerCantidadMujeresHombres(self):
        mujeres,hombres=0,0
        for ingreso in self.__listaIngresos:
            if(ingreso.getPersona().getGenero()=="FEMENINO"):
                mujeres +=1
            else:
                hombres +=1
                
        return mujeres,hombres
    
    def getListaSillas(self):
        return self.__listaSillas
    
    def getListaIngresos(self):
        return self.__listaIngresos
    
    def getNombre(self):
        return self.__nombre          
    
    def getCantidadSillas(self):
        return self.__cantidadSillas 
                