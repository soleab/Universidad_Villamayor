import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from pg import DB
import json
import time

conn = DB(dbname='UVM',user='secretario1',passwd='secretario1')

#TODAS LAS FUNCIONES ESTÁN IMPLEMENTADAS
def crear_usuario(body):
    """
    Crear un usuario
    Solo puede hacerlo el administrador de usuarios.
    :param body: Crear usuario
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
  
    dni = body.get("dni")
    email = body.get("email")
    psswrd = body.get("password")
    nombre = body.get("username")
    fecha = time.strftime("%d/%m/%y")
    consulta ='insert into public."Usuarios" values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (nombre,psswrd,fecha,email,dni)
    resultado = conn.query(consulta)
    return dni, email, psswrd, nombre


def delete_user(username):
    """
    Eliminar usuario
    Solo pude hacerlo el administrador de usuarios.
    :param username: Nombre de usuario que quiere ser borrado
    :type username: str

    :rtype: None
    """
    consulta ='delete from public."Usuarios" where public."Usuarios"."LoginID" = \'%s\'' % username
    resultado = conn.query(consulta)
    return 'Usuario eliminado correctamente'


def get_user_by_name(username):
    """
    Obtiene un usuario por su nombre de usuario
    
    :param username: Nombre de usuario que se desea buscar 
    :type username: str

    :rtype: User
    """
    consulta = 'select public."Usuarios"."LoginID",public."Usuarios"."Contraseña",public."Usuarios"."email"  from public."Usuarios" where public."Usuarios"."LoginID" = \'%s\'' % username
    resultado = conn.query(consulta)
    return json.dumps(resultado.getresult())


def logout_user():
    """
    Cerrar sesión
    

    :rtype: None
    """
    return 'Usuario desconectado'


def update_user(username, body):
    """
    Actualizar un usuario
    Solamente puede hacerlo el usuario loggeado.
    :param username: Nombre del usuario que quiere modificarse
    :type username: str
    :param body: Usuario a modificar
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()
    dni = body.get("dni")
    email = body.get("email")
    psswrd = body.get("password")
    nombre = body.get("username")

    consulta = 'UPDATE public."Usuarios" SET "LoginID" = \'%s\', "Contraseña"= \'%s\',email = \'%s\', dni=\'%s\' WHERE "LoginID" = \'%s\'' % (nombre,psswrd,email,dni, username)
    resultado= conn.query(consulta)
    return 'Usuario actualizado correctamente'
