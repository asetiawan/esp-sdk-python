# coding: utf-8

"""
    ESP Documentation

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.models.stat_signature import StatSignature


class TestStatSignature(unittest.TestCase):
    """ StatSignature unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatSignature(self):
        """
        Test StatSignature
        """
        model = esp_sdk.models.stat_signature.StatSignature()


if __name__ == '__main__':
    unittest.main()
