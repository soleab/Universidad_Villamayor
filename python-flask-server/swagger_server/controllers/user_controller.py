import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def crear_usuario(body):
    """
    Crear un usuario
    Solo puede hacerlo el administrador de usuarios.
    :param body: Crear usuario
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    return 'do some magic!'


def delete_user(username):
    """
    Eliminar usuario
    Solo pude hacerlo el administrador de usuarios.
    :param username: Nombre de usuario que quiere ser borrado
    :type username: str

    :rtype: None
    """
    return 'do some magic!'


def get_user_by_name(username):
    """
    Obtiene un usuario por su nombre de usuario
    
    :param username: Nombre de usuario que se desea buscar 
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def logout_user():
    """
    Cerrar sesión
    

    :rtype: None
    """
    return 'do some magic!'


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
        body = User.from_dict(connexion.request.get_json())
    return 'do some magic!'
