import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from pg import DB
import json

conn = DB(dbname='UVM',user='visitante',passwd='visitante')
#TODAS LAS OPERACIONES ESTÁN IMPLEMENTADAS
def get_grados_facultad(facultad):
    """
    Consultar los grados que hay en una facultad
    
    :param facultad: Informa de los grados de una facultad
    :type facultad: str

    :rtype: None
    """
    consulta= 'select public."Grados"."NombreGrado" from public."Facultades" inner join public."Grados" on public."Facultades".id = public."Grados".id where public."Facultades"."Nombre"= \'%s\'' % facultad
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult(),indent=4)

