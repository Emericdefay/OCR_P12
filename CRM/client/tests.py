# Django Libs:
from django.contrib.auth.models import User
# Django Rest Framework Libs:
from rest_framework.test import APITestCase
# Locals:
from user.models import (Saler, Support)


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
            - Support User
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

    def test_SaU_lc(self):
        """Test -> Empty list
        Saler user/
            + list clients
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 204)

    def test_SaU_cc(self):
        """Test
        Saler user/
            + create client
        """
        pass
    def test_SaU_rc_th(self):
        """Test
        Saler user/
            THROUGH/
                + retrieve client
        """
        pass

    def test_SaU_rc_nth(self):
        """Test
        Saler user/
            not THROUGH/
                - retrieve client
        """
        pass

    def test_SaU_uc_th(self):
        """Test
        Saler user/
            THROUGH/
                + update client
        """
        pass

    def test_SaU_uc_nth(self):
        """Test
        Saler user/
            not THROUGH/
                - update client
        """
        pass

    def test_SaU_dc(self):
        """Test
        Saler user/
            - delete client
        """
        pass


    def test_SuU_lc(self):
        """Test
        Support User/
            + list client
        """
    def test_SuU_cc(self):
        """Test
        Support User/
            - create client
        """
        pass

    def test_SuU_rc_th(self):
        """Test
        Support User/
            THROUGH/
                + retrieve client
        """
        pass

    def test_SuU_rc_nth(self):
        """Test
        Support User/
            not THROUGH
                - retrieve client
        """
        pass

    def test_SuU_uc(self):
        """Test
        Support User/
            - update client
        """
        pass

    def test_SuU_dc(self):
        """Test
        Support User/
            - delete client
        """
        pass


    def test_UWoR_lc(self):
        """Test
        User Without Role/
            - list clients
        """
        pass

    def test_UWoR_cc(self):
        """Test
        User Without Role/
            - create client
        """
        pass

    def test_UWoR_rc(self):
        """Test
        User Without Role/
            - retrieve client
        """
        pass

    def test_UWoR_uc(self):
        """Test
        User Without Role/
            - update client
        """
        pass

    def test_UWoR_dc(self):
        """Test
        User Without Role/
            - delete client
        """
        pass


    def test_UU_lc(self):
        """Test
        Unauthenticated User/
            - list clients
        """
        pass

    def test_UU_cc(self):
        """Test
        Unauthenticated User/
            - create client
        """
        pass

    def test_UU_rc(self):
        """Test
        Unauthenticated User/
            - retrieve client
        """
        pass

    def test_UU_uc(self):
        """Test
        Unauthenticated User/
            - update client
        """
        pass

    def test_UU_dc(self):
        """Test
        Unauthenticated User/
            - delete client
        """
        pass
