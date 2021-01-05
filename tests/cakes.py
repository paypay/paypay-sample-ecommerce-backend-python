from unittest import TestCase, mock
from app import app

class CakesTests(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()


    @mock.patch.dict("os.environ", {"API_KEY": "TEST"})
    def test_get_cakes(self):
        # When
        response = self.app.get('/cakes', headers={"Content-Type": "application/json"})
        # Then
        self.assertEqual(200, response.status_code)