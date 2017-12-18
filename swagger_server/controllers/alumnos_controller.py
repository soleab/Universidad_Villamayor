import connexion
from swagger_server.models.alumno import Alumno
from swagger_server.models.matricula import Matricula
from swagger_server.models.pago import Pago
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from pg import DB
import json
import time

conn = DB(dbname='UVM',user='visitante',passwd='visitante')

#FALTA POR IMPLEMENTAR: matriculacion, modificar_alumno y pago
def crear_alumno(alumno=None):
    """
    crear un nuevo alumno
    
    :param alumno: Crear Alumno
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = (connexion.request.get_json())
        
    contraseña = alumno.get("Contraseña")
    dni = alumno.get("DNI")
    fecha_nac = alumno.get("FechaNacimiento")
    grado_id= alumno.get("Grado")
    nombre = alumno.get("NombreCompleto")
    usuario = alumno.get("Usuario")
    email = alumno.get("email")
    fecha = time.strftime("%d/%m/%y")
    
    consulta ='insert into public."Usuarios" values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (usuario,contraseña,fecha,email,dni)
    resultado = conn.query(consulta)
    print (usuario)
    cons='insert into public."Alumnos" values (\'%s\',\'%s\',\'%s\',%d,\'%s\')' % (nombre, dni, fecha_nac, grado_id, usuario)
    res = conn.query(cons)
    return 'Alumno creado correctamente'


def get_datos(dni):
    """
    Consultar los datos de un alumno
    
    :param dni: Da informacion acerca de un alumno
    :type dni: str

    :rtype: None
    """
    consulta = 'select public."Alumnos"."NombreCompleto",public."Alumnos"."Dni",public."Alumnos"."GradoID",public."Alumnos"."LoginID" from public."Alumnos" where public."Alumnos"."Dni"= \'%s\'' % dni
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult())


def get_matricula(dni):
    """
    Consultar matricula
    
    :param dni: Muestra la información de la matrícula de un alumno
    :type dni: str

    :rtype: None
    """
    consulta = 'select public."Matricula"."MatriculaID",public."Matricula"."PrecioTotal",public."Matricula"."Estado",public."Matricula"."FormaPago",public."Matricula"."Reserva",public."Matricula"."Dni",public."Matricula"."GradoID"from public."Matricula" inner join public."Alumnos" on public."Matricula"."Dni" = public."Alumnos"."Dni"where public."Alumnos"."Dni"= %s' %dni
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult())


def matriculacion(matricula=None):
    """
    Matricularse
    
    :param matricula: Crear Matricula
    :type matricula: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        matricula = Matricula.from_dict(connexion.request.get_json())
    return 'do some magic!'


def modificar_alumno(dni):
    """
    Modificar alumno
    
    :param dni: dni del alumno que se quiere modificar
    :type dni: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        dni = Alumno.from_dict(connexion.request.get_json())
    return 'do some magic!'


def pago(usuario=None):
    """
    Reserva de plaza o pago de matrícula
    
    :param usuario: pagar la reserva o la matrícula
    :type usuario: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        usuario = Pago.from_dict(connexion.request.get_json())
    return 'do some magic!'
