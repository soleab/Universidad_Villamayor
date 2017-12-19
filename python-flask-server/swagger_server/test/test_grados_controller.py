# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.asignatura import Asignatura
from swagger_server.models.grado import Grado
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestGradosController(BaseTestCase):
    """ GradosController integration test stubs """

    def test_crear_asignatura(self):
        """
        Test case for crear_asignatura

        Añadir una asignatura a un grado
        """
        grado = Asignatura()
        response = self.client.open('/Grados/Asignaturas',
                                    method='POST',
                                    data=json.dumps(grado),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_grado(self):
        """
        Test case for crear_grado

        Añadir un grado
        """
        facultad = Grado()
        response = self.client.open('/Grados',
                                    method='POST',
                                    data=json.dumps(facultad),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_asignaturas(self):
        """
        Test case for get_asignaturas

        Consultar asignaturas por grado
        """
        query_string = [('grado', 'grado_example')]
        response = self.client.open('/Grados/Asignaturas',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_grados(self):
        """
        Test case for get_grados

        Consultar grados
        """
        response = self.client.open('/Grados',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
