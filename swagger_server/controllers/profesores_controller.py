import connexion
from swagger_server.models.matricula_asignaturas import MatriculaAsignaturas
from swagger_server.models.profesor import Profesor
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from pg import DB
import json

conn = DB(dbname='UVM',user='profe1',passwd='profe1')

#FALTAN POR IMPLEMENTAR: añadir_nota, crear_profesor
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
    consulta = 'select public."Profesores"."NombreCompleto",public."Profesores"."Dni",public."Profesores"."Investigacion",public."Profesores"."Docencia",public."Profesores"."LoginID",public."Profesores"."CategoriaId",public."Profesores"."DepartamentoId" from public."Profesores" where public."Profesores"."Dni"= \'%s\'' % dni
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult())
