import google.auth.credentials
import google_auth_httplib2
import httplib2
import oauth2client.client
import unittest
from unittest import mock
from googleapiclient import _auth
from operations import *
import sys
from io import StringIO
import subprocess

class TestAuthWithOAuth2Client(unittest.TestCase):
    def setUp(self):
        _auth.HAS_GOOGLE_AUTH = False
        _auth.HAS_OAUTH2CLIENT = True
        self.held, sys.stdout = sys.stdout, StringIO()
    def tearDown(self):
        _auth.HAS_GOOGLE_AUTH = True
        _auth.HAS_OAUTH2CLIENT = True

    def test_credentials_from_file(self):
        with self.assertRaises(EnvironmentError):
            credentials = _auth.credentials_from_file("credentials.json")
    def test_default_credentials_with_scopes_and_quota_project(self):
        with self.assertRaises(EnvironmentError):
            credentials = _auth.default_credentials(
                scopes=["1", "2"], quota_project_id="my-project"
            )
    def test_with_scopes_scoped(self):
        credentials = mock.Mock(spec=oauth2client.client.GoogleCredentials)
        credentials.create_scoped_required.return_value = True
        returned = _auth.with_scopes(credentials, mock.sentinel.scopes)
        self.assertNotEqual(credentials, returned)
        self.assertEqual(returned, credentials.create_scoped.return_value)
        credentials.create_scoped.assert_called_once_with(mock.sentinel.scopes)
    def test_authorized_http(self):
        credentials = mock.Mock(spec=oauth2client.client.Credentials)
        authorized_http = _auth.authorized_http(credentials)
        http = credentials.authorize.call_args[0][0]
        self.assertEqual(authorized_http, credentials.authorize.return_value)
        self.assertIsInstance(http, httplib2.Http)
        self.assertIsInstance(http.timeout, int)
        self.assertGreater(http.timeout, 0)

    from unittest.mock import patch
    @patch('builtins.print')
    def test_download(self, mock_print):
        credentials = mock.Mock(spec=oauth2client.client.Credentials)
        authorized_http = _auth.authorized_http(credentials)
        http = credentials.authorize.call_args[0][0]
        expected_output = 'Download successful'
        download('DSC_6549.JPG')
        mock_print.asser_called_with(expected_output)