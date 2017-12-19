import connexion
from swagger_server.models.alumno import Alumno
from swagger_server.models.matricula import Matricula
from swagger_server.models.pago import Pago
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_alumno(alumno=None):
    """
    crear un nuevo alumno
    
    :param alumno: Crear Alumno
    :type alumno: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        alumno = Alumno.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_datos(dni):
    """
    Consultar los datos de un alumno
    
    :param dni: Da informacion acerca de un alumno
    :type dni: str

    :rtype: None
    """
    return 'do some magic!'


def get_matricula(dni):
    """
    Consultar matricula
    
    :param dni: Muestra la información de la matrícula de un alumno
    :type dni: str

    :rtype: None
    """
    return 'do some magic!'


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
