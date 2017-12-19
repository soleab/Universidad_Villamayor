# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Pago(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identificador: int=None, plazo: int=None, importe: float=None, pagado: bool=None, fecha_orden: str=None, fecha_vencimiento: str=None, id_matricula: int=None):
        """
        Pago - a model defined in Swagger

        :param identificador: The identificador of this Pago.
        :type identificador: int
        :param plazo: The plazo of this Pago.
        :type plazo: int
        :param importe: The importe of this Pago.
        :type importe: float
        :param pagado: The pagado of this Pago.
        :type pagado: bool
        :param fecha_orden: The fecha_orden of this Pago.
        :type fecha_orden: str
        :param fecha_vencimiento: The fecha_vencimiento of this Pago.
        :type fecha_vencimiento: str
        :param id_matricula: The id_matricula of this Pago.
        :type id_matricula: int
        """
        self.swagger_types = {
            'identificador': int,
            'plazo': int,
            'importe': float,
            'pagado': bool,
            'fecha_orden': str,
            'fecha_vencimiento': str,
            'id_matricula': int
        }

        self.attribute_map = {
            'identificador': 'identificador',
            'plazo': 'plazo',
            'importe': 'importe',
            'pagado': 'pagado',
            'fecha_orden': 'fechaOrden',
            'fecha_vencimiento': 'fechaVencimiento',
            'id_matricula': 'idMatricula'
        }

        self._identificador = identificador
        self._plazo = plazo
        self._importe = importe
        self._pagado = pagado
        self._fecha_orden = fecha_orden
        self._fecha_vencimiento = fecha_vencimiento
        self._id_matricula = id_matricula

    @classmethod
    def from_dict(cls, dikt) -> 'Pago':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pago of this Pago.
        :rtype: Pago
        """
        return deserialize_model(dikt, cls)

    @property
    def identificador(self) -> int:
        """
        Gets the identificador of this Pago.
        identificador del pago

        :return: The identificador of this Pago.
        :rtype: int
        """
        return self._identificador

    @identificador.setter
    def identificador(self, identificador: int):
        """
        Sets the identificador of this Pago.
        identificador del pago

        :param identificador: The identificador of this Pago.
        :type identificador: int
        """

        self._identificador = identificador

    @property
    def plazo(self) -> int:
        """
        Gets the plazo of this Pago.
        plazo de pago (uno, dos o tres)

        :return: The plazo of this Pago.
        :rtype: int
        """
        return self._plazo

    @plazo.setter
    def plazo(self, plazo: int):
        """
        Sets the plazo of this Pago.
        plazo de pago (uno, dos o tres)

        :param plazo: The plazo of this Pago.
        :type plazo: int
        """

        self._plazo = plazo

    @property
    def importe(self) -> float:
        """
        Gets the importe of this Pago.
        cantidad a pagar en ese plazo

        :return: The importe of this Pago.
        :rtype: float
        """
        return self._importe

    @importe.setter
    def importe(self, importe: float):
        """
        Sets the importe of this Pago.
        cantidad a pagar en ese plazo

        :param importe: The importe of this Pago.
        :type importe: float
        """

        self._importe = importe

    @property
    def pagado(self) -> bool:
        """
        Gets the pagado of this Pago.
        indica si se ha pagado

        :return: The pagado of this Pago.
        :rtype: bool
        """
        return self._pagado

    @pagado.setter
    def pagado(self, pagado: bool):
        """
        Sets the pagado of this Pago.
        indica si se ha pagado

        :param pagado: The pagado of this Pago.
        :type pagado: bool
        """

        self._pagado = pagado

    @property
    def fecha_orden(self) -> str:
        """
        Gets the fecha_orden of this Pago.

        :return: The fecha_orden of this Pago.
        :rtype: str
        """
        return self._fecha_orden

    @fecha_orden.setter
    def fecha_orden(self, fecha_orden: str):
        """
        Sets the fecha_orden of this Pago.

        :param fecha_orden: The fecha_orden of this Pago.
        :type fecha_orden: str
        """

        self._fecha_orden = fecha_orden

    @property
    def fecha_vencimiento(self) -> str:
        """
        Gets the fecha_vencimiento of this Pago.
        último día para pagar la matrícula, generado automáticamente

        :return: The fecha_vencimiento of this Pago.
        :rtype: str
        """
        return self._fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento: str):
        """
        Sets the fecha_vencimiento of this Pago.
        último día para pagar la matrícula, generado automáticamente

        :param fecha_vencimiento: The fecha_vencimiento of this Pago.
        :type fecha_vencimiento: str
        """

        self._fecha_vencimiento = fecha_vencimiento

    @property
    def id_matricula(self) -> int:
        """
        Gets the id_matricula of this Pago.
        identificador de la matrícula a la que va asociada el pago

        :return: The id_matricula of this Pago.
        :rtype: int
        """
        return self._id_matricula

    @id_matricula.setter
    def id_matricula(self, id_matricula: int):
        """
        Sets the id_matricula of this Pago.
        identificador de la matrícula a la que va asociada el pago

        :param id_matricula: The id_matricula of this Pago.
        :type id_matricula: int
        """

        self._id_matricula = id_matricula

