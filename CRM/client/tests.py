# Django Libs:
from django.contrib.auth.models import User
# Django Rest Framework Libs:
from rest_framework.test import APITestCase
# Locals:
from client.models import Client
from user.models import (Saler, Support, SupportTHROUGH)


class TestClient(APITestCase):
    """Tests for client management.
    
    Legend :
        '+': Has permission
        '=': Permission if linked to client
        '-': No permission

    Tests:
        (Sa)ler (U)ser : (SaU)
            + list clients (lc)
            + create client (cc)
            = retrieve client (rc)
            = update client (uc)
            - delete client (dc)
        (Su)pport (U)ser : (SuU)
            + list clients (lc)
            - create client (cc)
            = retrieve client (rc)
            - update client (uc)
            - delete client (dc)
        (U)ser (W)ith(o)ut (R)ole : (UWoR)
            - list clients (lc)
            - create client (cc)
            - retrieve client (rc)
            - update client (uc)
            - delete client (dc)
        (U)nauthenticated (U)ser : (UU)
            - list clients (lc)
            - create client (cc)
            - retrieve client (rc)
            - update client (uc)
            - delete client (dc)
    """
    def setUp(self):
        """Setup
        
        Users:
            - Saler User 
            - Saler User NOT THROUGH
            - Support User THROUGH
            - Support User NOT THROUGH
            - User without role
        """
        # (Saler) User
        user_form = {
            'username': 'saler',
            'last_name': 'saler',
            'first_name': 'saler',
            'password': 'Motdepasse123',
            'email': 'test@test.com',
        }
        user = User.objects.create_user(**user_form)
        user.save()
        # Make him saler
        user = User.objects.get(username='saler')
        saler_form = {'user': user}
        saler_user = Saler(**saler_form)
        saler_user.save()

        # (Saler) User NOT THROUGH
        user_form = {
            'username': 'salerNTH',
            'last_name': 'saler',
            'first_name': 'saler',
            'password': 'Motdepasse123',
            'email': 'test@test.com',
        }
        user = User.objects.create_user(**user_form)
        user.save()
        # Make him saler
        user = User.objects.get(username='salerNTH')
        saler_form = {'user': user}
        saler_user = Saler(**saler_form)
        saler_user.save()

        # (Support) User
        user_form = {
            'username': 'support',
            'last_name': 'support',
            'first_name': 'support',
            'password': 'Motdepasse123',
            'email': 'test@test.com',
        }
        user = User.objects.create_user(**user_form)
        user.save()
        # Make him support
        user = User.objects.get(username='support')
        support_form = {'user': user}
        support_user = Support(**support_form)
        support_user.save()

        # (Support) User NOT THROUGH
        user_form = {
            'username': 'supportNTH',
            'last_name': 'support',
            'first_name': 'support',
            'password': 'Motdepasse123',
            'email': 'test@test.com',
        }
        user = User.objects.create_user(**user_form)
        user.save()
        # Make him support
        user = User.objects.get(username='supportNTH')
        support_form = {'user': user}
        support_user = Support(**support_form)
        support_user.save()

        # User without Role
        user_form = {
            'username': 'user',
            'last_name': 'user',
            'first_name': 'user',
            'password': 'Motdepasse123',
            'email': 'test@test.com',
        }
        user = User.objects.create_user(**user_form)
        user.save()

    def test_SaU_lc_e(self):
        """Test -> Empty list
        Saler user/
            + list clients
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 204)

    def test_SaU_lc_ne(self):
        """Test -> Not empty list
        Saler user/
            + list clients
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_cc(self):
        """Test
        Saler user/
            + create client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        response = self.client.post(path=url, data=client_form)
        self.assertEqual(response.status_code, 201)

    def test_SaU_rc_th(self):
        """Test
        Saler user/
            THROUGH/
                + retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_rc_nth(self):
        """Test
        Saler user/
            not THROUGH/
                - retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)
        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SaU_uc_th(self):
        """Test
        Saler user/
            THROUGH/
                + update client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)
        client_update = {
            'first_name': 'another test',
        }
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.put(path=url, data=client_update)
        self.assertEqual(response.status_code, 200)

    def test_SaU_uc_nth(self):
        """Test
        Saler user/
            not THROUGH/
                - update client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        client_update = {
            'first_name': 'another test',
        }
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.put(path=url, data=client_update)
        self.assertEqual(response.status_code, 403)

    def test_SaU_dc(self):
        """Test
        Saler user/
            - delete client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)


    def test_SuU_lc_e(self):
        """Test -> Empty list
        Support User/
            + list client
        """
        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 204)

    def test_SuU_lc_ne(self):
        """Test -> Empty list
        Support User/
            + list client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)


    def test_SuU_cc(self):
        """Test
        Support User/
            - create client
        """
        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        response = self.client.post(path=url, data=client_form)
        self.assertEqual(response.status_code, 403)

    def test_SuU_rc_th(self):
        """Test
        Support User/
            THROUGH/
                + retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='support')
        client = Client.objects.get(first_name='test')
        
        # Make support THROUGH
        through = {
            'user': user,
            'client': client,
        }
        support_through = SupportTHROUGH(**through)
        support_through.save()

        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SuU_rc_nth(self):
        """Test
        Support User/
            not THROUGH
                - retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='supportNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SuU_uc(self):
        """Test
        Support User/
            - update client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        client = Client.objects.get(first_name='test')
        
        # Make support THROUGH
        through = {
            'user': user,
            'client': client,
        }
        support_through = SupportTHROUGH(**through)
        support_through.save()

        url = 'http://127.0.0.1:8000/client/1/'
        client_update = {
            'first_name': 'test',
        }
        response = self.client.put(path=url, data=client_update)
        self.assertEqual(response.status_code, 403)

    def test_SuU_dc(self):
        """Test
        Support User/
            - delete client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='support')
        client = Client.objects.get(first_name='test')
        
        # Make support THROUGH
        through = {
            'user': user,
            'client': client,
        }
        support_through = SupportTHROUGH(**through)
        support_through.save()

        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)


    def test_UWoR_lc(self):
        """Test - empty list
        User Without Role/
            - list clients
        """
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_lc_ne(self):
        """Test -> not empty list
        User Without Role/
            - list clients
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)
        
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_cc(self):
        """Test
        User Without Role/
            - create client
        """
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        response = self.client.post(path=url, data=client_form)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_rc(self):
        """Test
        User Without Role/
            - retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_uc(self):
        """Test
        User Without Role/
            - update client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        client_update = {
            'first_name': 'another test',
        }
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.put(path=url, data=client_update)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_dc(self):
        """Test
        User Without Role/
            - delete client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)


    def test_UU_lc(self):
        """Test
        Unauthenticated User/
            - list clients
        """
        url = 'http://127.0.0.1:8000/client/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_cc(self):
        """Test
        Unauthenticated User/
            - create client
        """
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        response = self.client.post(path=url, data=client_form)
        self.assertEqual(response.status_code, 401)

    def test_UU_rc(self):
        """Test
        Unauthenticated User/
            - retrieve client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_uc(self):
        """Test
        Unauthenticated User/
            - update client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/'
        client_update = {
            'first_name': 'another test',
        }
        response = self.client.put(path=url, data=client_update)
        self.assertEqual(response.status_code, 401)

    def test_UU_dc(self):
        """Test
        Unauthenticated User/
            - delete client
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        client_form = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        self.client.post(path=url, data=client_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 401)
