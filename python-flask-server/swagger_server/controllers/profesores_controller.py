import connexion
from swagger_server.models.matricula_asignaturas import MatriculaAsignaturas
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def añadir_nota(dni):
    """
    Añadir nota de un alumno
    
    :param dni: Crear Alumno
    :type dni: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        dni = MatriculaAsignaturas.from_dict(connexion.request.get_json())
    return 'do some magic!'


def crear_profesor(profesor=None):
    """
    Añadir un nuevo profesor
    
    :param profesor: Crear profesor
    :type profesor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        profesor = Profesor.from_dict(connexion.request.get_json())
    return 'do some magic!'


def info_profesor(dni):
    """
    Obtener la información referente a un profesor
    
    :param dni: información del profesor solicitado por dni
    :type dni: str

    :rtype: None
    """
    return 'do some magic!'
