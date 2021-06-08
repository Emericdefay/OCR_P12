# Std Libs:
import datetime
# Django Libs:
from django.contrib.auth.models import User
# Django Rest Framework Libs:
from rest_framework.test import APITestCase
# Locals:
from client.models import Client
from user.models import (Saler,
                         SalerTHROUGH,
                         Support)


class TestContract(APITestCase):
    """Tests for contract management.
    
    Legend :
        '+': Has permission
        '=': Permission if linked to contract
        '-': No permission

    Tests:
        (Sa)ler (U)ser : (SaU)
            + list contracts (lc)
            = create contract (cc)
            = retrieve contract (rc)
            = update contract (uc)
            - delete contract (dc)
        (Su)pport (U)ser : (SuU)
            + list contracts (lc)
            - create contract (cc)
            - retrieve contract (rc)
            - update contract (uc)
            - delete contract (dc)
        (U)ser (W)ith(o)ut (R)ole : (UWoR)
            - list contracts (lc)
            - create contract (cc)
            - retrieve contract (rc)
            - update contract (uc)
            - delete contract (dc)
        (U)nauthenticated (U)ser : (UU)
            - list contracts (lc)
            - create contract (cc)
            - retrieve contract (rc)
            - update contract (uc)
            - delete contract (dc)
    """
    def setUp(self):
        """Setup

        Users:
            - Saler
            - Saler not THROUGH
            - Support
            - Support not THROUGH
            - User without Role
        Client:
            - Client
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

        # (Saler) User not THROUGH
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

        # Client
        user = User.objects.get(username='saler')
        client_form = {
            'sales_contact': user,
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@test.com',
            'phone': 'test',
            'mobile': 'test',
            'company_name': 'test',
        }
        client = Client(**client_form)
        client.save()

        # Saler THROUGH
        through_form = {
            'user': user,
            'client': client,
        }
        through = SalerTHROUGH(**through_form)
        through.save()


    def test_SaU_lc(self):
        """Test -> no contract
            Saler User/
                + list contracts
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 204)

    def test_SaU_lc(self):
        """Test -> available contract(s)
            Saler User/
                + list contracts
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        url = 'http://127.0.0.1:8000/client/1/contract/'
        self.client.post(path=url, data=contract_form)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_cc_th(self):
        """Test
            Saler User/
                THROUGH/
                    + create contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        response = self.client.post(path=url, data=contract_form)
        self.assertEqual(response.status_code, 201)

    def test_SaU_cc_nth(self):
        """Test
            Saler User/
                not THROUGH/
                    - create contract
        """
        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        response = self.client.post(path=url, data=contract_form)
        self.assertEqual(response.status_code, 403)

    def test_SaU_rc_th(self):
        """Test
            Saler User/
                THROUGH/
                    + retrieve contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_rc_nth(self):
        """Test
            Saler User/
                not THROUGH/
                    - retrieve contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SaU_uc_th(self):
        """Test
            Saler User/
                THROUGH/
                    + update contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        contract_update = {
            'status': True,
        }
        response = self.client.put(path=url, data=contract_update)
        self.assertEqual(response.status_code, 200)

    def test_SaU_uc_nth(self):
        """Test
            Saler User/
                not THROUGH/
                    - update contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        contract_update = {
            'status': True,
        }
        response = self.client.put(path=url, data=contract_update)
        self.assertEqual(response.status_code, 403)

    def test_SaU_dc(self):
        """Test
            Saler User/
                - delete contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SuU_lc(self):
        """Test
            Support User/
                + list contract(s)
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SuU_cc(self):
        """Test
            Support User/
                - contract
        """
        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        response = self.client.post(path=url, data=contract_form)
        self.assertEqual(response.status_code, 403)

    def test_SuU_rc(self):
        """Test
            Support User/
                - retrieve contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SuU_uc(self):
        """Test
            Support User/
                - update contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        contract_update = {
            'status': True,
        }
        response = self.client.put(path=url, data=contract_update)
        self.assertEqual(response.status_code, 403)

    def test_SuU_dc(self):
        """Test
            Support User/
                - contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_lc(self):
        """Test
            User Without Role/
                - list contract(s)
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_cc(self):
        """Test
            User Without Role/
                - create contract
        """
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }        
        response = self.client.post(path=url, data=contract_form)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_rc(self):
        """Test
            User Without Role/
                - retrieve contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_uc(self):
        """Test
            User Without Role/
                - update contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        contract_update = {
            'status': True,
        }
        response = self.client.put(path=url, data=contract_update)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_dc(self):
        """Test
            User Without Role/
                - delete contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UU_lc(self):
        """Test
            Unauthenticate User/
                - list contracts
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_cc(self):
        """Test
            Unauthenticate User/
                - create contract
        """
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        response = self.client.post(path=url, data=contract_form)
        self.assertEqual(response.status_code, 401)

    def test_UU_rc(self):
        """Test
            Unauthenticate User/
                - retrieve contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_uc(self):
        """Test
            Unauthenticate User/
                - update contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        contract_update = {
            'status': True,
        }
        response = self.client.put(path=url, data=contract_update)
        self.assertEqual(response.status_code, 401)

    def test_UU_dc(self):
        """Test
            Unauthenticate User/
                - delete contract
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'status': False,
            'amount': 10.0,
            'payment_due': d,
        }
        self.client.post(path=url, data=contract_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 401)
