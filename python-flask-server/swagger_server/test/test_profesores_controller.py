# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.matricula_asignaturas import MatriculaAsignaturas
from swagger_server.models.profesor import Profesor
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProfesoresController(BaseTestCase):
    """ ProfesoresController integration test stubs """

    def test_añadir_nota(self):
        """
        Test case for añadir_nota

        Añadir nota de un alumno
        """
        dni = MatriculaAsignaturas()
        response = self.client.open('/Profesores/Grupos/Alumnos/Notas',
                                    method='POST',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_crear_profesor(self):
        """
        Test case for crear_profesor

        Añadir un nuevo profesor
        """
        profesor = Profesor()
        response = self.client.open('/Profesores',
                                    method='POST',
                                    data=json.dumps(profesor),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_info_profesor(self):
        """
        Test case for info_profesor

        Obtener la información referente a un profesor
        """
        query_string = [('dni', 'dni_example')]
        response = self.client.open('/Profesores',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
