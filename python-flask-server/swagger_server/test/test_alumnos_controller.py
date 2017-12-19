# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.alumno import Alumno
from swagger_server.models.matricula import Matricula
from swagger_server.models.pago import Pago
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAlumnosController(BaseTestCase):
    """ AlumnosController integration test stubs """

    def test_crear_alumno(self):
        """
        Test case for crear_alumno

        crear un nuevo alumno
        """
        alumno = Alumno()
        response = self.client.open('/Alumnos',
                                    method='POST',
                                    data=json.dumps(alumno),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_datos(self):
        """
        Test case for get_datos

        Consultar los datos de un alumno
        """
        query_string = [('dni', 'dni_example')]
        response = self.client.open('/Alumnos',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_matricula(self):
        """
        Test case for get_matricula

        Consultar matricula
        """
        query_string = [('dni', 'dni_example')]
        response = self.client.open('/Alumnos/Matricula',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_matriculacion(self):
        """
        Test case for matriculacion

        Matricularse
        """
        matricula = Matricula()
        response = self.client.open('/Alumnos/Matricula',
                                    method='POST',
                                    data=json.dumps(matricula),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_modificar_alumno(self):
        """
        Test case for modificar_alumno

        Modificar alumno
        """
        dni = Alumno()
        response = self.client.open('/Alumnos',
                                    method='PUT',
                                    data=json.dumps(dni),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_pago(self):
        """
        Test case for pago

        Reserva de plaza o pago de matrícula
        """
        usuario = Pago()
        response = self.client.open('/Alumnos/Pagos',
                                    method='POST',
                                    data=json.dumps(usuario),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
