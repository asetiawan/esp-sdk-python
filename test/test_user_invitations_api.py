# coding: utf-8

"""
    ESP Documentation

    The Evident Security Platform API (version 2.0) is designed to allow users granular control over their Amazon Web Service security experience by allowing them to review alerts, monitor signatures, and create custom signatures.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import esp_sdk
from esp_sdk.rest import ApiException
from esp_sdk.apis.user_invitations_api import UserInvitationsApi


class TestUserInvitationsApi(unittest.TestCase):
    """ UserInvitationsApi unit test stubs """

    def setUp(self):
        self.api = esp_sdk.apis.user_invitations_api.UserInvitationsApi()

    def tearDown(self):
        pass

    def test_update(self):
        """
        Test case for update

        A successful call to this API updates and accepts a User Invitation
        """
        pass


if __name__ == '__main__':
    unittest.main()