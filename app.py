from modelo.sala import Sala
from modelo.persona import Persona
import datetime

import os

miSala=Sala("SENA",2)

def ingresoSala():
    os.system("cls")
    print("Registrar Ingreso a la Sala")
    id = input("Ingrese identificación de la persona: ")
    nombre = input("Ingrese nombre de la persona: ")
    correo = input("Ingrese correo electrónico de la persona: ")
    genero = input("Ingrese genero de la persona (Femenino/Masculino): ").upper()
    estado,mensaje=miSala.registrarIngreso(id,nombre,correo,genero)
    print(mensaje)
    

def consultarSilla():
    os.system("cls")
    print("Consultar Silla")
    numero= int(input(f"Ingrese número de silla a consultar de 1 a {miSala.getCantidadSillas()}: "))
    persona = miSala.obtenerDatosPersonaSilla(numero)
    if(type(persona)==Persona):
        print(f"Datos de la Persona ubicada en la Silla # {numero}")
        print(f"Identificación: {persona.getIdentificacion()}")
        print(f"Nombre: {persona.getNombre()}")
        print(f"Correo: {persona.getCorreo()}")
        print(f"Genero: {persona.getGenero()}")
    else:
        print(persona)
    
def cantidadPersonasGenero():
    os.system("cls")
    print("Consultar Cantidad Personas Genero")
    mujeres,hombres= miSala.obtenerCantidadMujeresHombres()
    print(f"Cantidad Mujeres {mujeres}")
    print(f"Cantidad Hombres {hombres}")

def datosPersonasSala():
    os.system("cls")
    print("Datos Personas en la Sala")
    for ingreso in miSala.getListaIngresos():
        print(f"Nombre: {ingreso.getPersona().getNombre()}")
        print(f"Silla: {ingreso.getSilla().getNumero()}")
        print(f"FechaIngreso: {ingreso.getFechaHora().strftime('%x')}")
        print(f"HoraIngreso: {ingreso.getFechaHora().strftime('%X')}")
        print("*"*50)
        

def menu():
    while(True):
        os.system("cls")
        print(f"\t\tGESTIÓN SALA {miSala.getNombre()}")
        print(f"\t1. Registrar Ingreso Sala")
        print(f"\t2. Consultar Silla")
        print(f"\t3. Cantidad Personas Genero")
        print(f"\t4. Datos Personas en Sala")
        print(f"\t5. Salir")
        opcion=int(input("\tIngrese opción: "))
        if(opcion==1):
            ingresoSala()
        elif(opcion==2):
            consultarSilla()
        elif(opcion==3):
            cantidadPersonasGenero()
        elif(opcion==4):
            datosPersonasSala()
        elif(opcion==5):
            print("salir......")
            break
        else:
            print("Opción no valida...")
                        
        input("Presione Enter para continuar")

menu()