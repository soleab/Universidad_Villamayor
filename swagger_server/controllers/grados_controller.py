import connexion
from swagger_server.models.asignatura import Asignatura
from swagger_server.models.grado import Grado
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from pg import DB
import json

conn=DB(dbname='UVM',user='visitante',passwd='visitante')

#FALTAN POR IMPLEMENTAR: crear_asignatura, crear_grado
def crear_asignatura(grado):
    """
    Añadir una asignatura a un grado
    Solo puede hacerlo el administrador de usuarios.
    :param grado: Crear Asignatura
    :type grado: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        grado = Asignatura.from_dict(connexion.request.get_json())
    return 'do some magic!'


def crear_grado(facultad):
    """
    Añadir un grado
    Solo puede hacerlo el administrador de usuarios.
    :param facultad: Crear Grado
    :type facultad: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        facultad = Grado.from_dict(connexion.request.get_json())
    return 'do some magic!'


def get_asignaturas(grado):
    """
    Consultar asignaturas por grado
    
    :param grado: Informa de las asignaturas de un grado
    :type grado: str

    :rtype: None
    """
    consulta= 'select public."Asignaturas"."AsignaturaID", public."Asignaturas"."Nombre", public."Asignaturas"."Creditos",public."Asignaturas"."Tipo",public."Asignaturas"."Curso",public."Asignaturas"."Semestre",public."Asignaturas"."GradoID"from public."Asignaturas" inner join public."Grados" on public."Asignaturas"."GradoID" = public."Grados"."GradoID"where public."Grados"."NombreGrado" = \'%s\'' % grado  
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult())


def get_grados():
    """
    Consultar grados
    

    :rtype: None
    """
    consulta= 'Select * from public."Grados"'
    resultado= conn.query(consulta)
    return json.dumps(resultado.getresult())

