# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestFacultadController(BaseTestCase):
    """ FacultadController integration test stubs """

    def test_get_grados_facultad(self):
        """
        Test case for get_grados_facultad

        Consultar los grados que hay en una facultad
        """
        query_string = [('facultad', 'facultad_example')]
        response = self.client.open('/Facultad',
                                    method='GET',
                                    content_type='application/json',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
