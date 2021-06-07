# Django Rest Framework Libs:
from rest_framework.test import APITestCase


class TestUser(APITestCase):
    """User tests

    Since users cannot signin =>
    Connection tests need to fail.
    """
    def test_login_fail(self):
        """Login failure
        Attempt : 401
        """
        user_form = {
            'username': 'test_saler',
            'password': 'Motdepasse123',
        }
        url = 'http://127.0.0.1:8000/login/'
        response = self.client.post(path=url, data=user_form)
        self.assertEqual(response.status_code, 401)
