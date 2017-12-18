# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUserController(BaseTestCase):
    """ UserController integration test stubs """

    def test_crear_usuario(self):
        """
        Test case for crear_usuario

        Crear un usuario
        """
        body = User()
        response = self.client.open('/user',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_user(self):
        """
        Test case for delete_user

        Eliminar usuario
        """
        response = self.client.open('/user/{username}'.format(username='username_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_user_by_name(self):
        """
        Test case for get_user_by_name

        Obtiene un usuario por su nombre de usuario
        """
        response = self.client.open('/user/{username}'.format(username='username_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_logout_user(self):
        """
        Test case for logout_user

        Cerrar sesión
        """
        response = self.client.open('/user/logout',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_user(self):
        """
        Test case for update_user

        Actualizar un usuario
        """
        body = User()
        response = self.client.open('/user/{username}'.format(username='username_example'),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
