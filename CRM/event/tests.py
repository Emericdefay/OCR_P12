# Std Libs:
import datetime
# Django Libs:
from django.contrib.auth.models import User
# Django Rest Framework Libs:
from rest_framework.test import APITestCase
# Locals:
from client.models import Client
from contract.models import Contract
from event.models import Event
from user.models import (Saler,
                         SalerTHROUGH,
                         Support,
                         SupportTHROUGH)


class TestEvent(APITestCase):
    """Tests for event management.
    
    Legend :
        '+': Has permission
        '=': Permission if linked to event
        '-': No permission

    Tests:
        (Sa)ler (U)ser : (SaU)
            + list events (le)
            = create event (ce)
            = retrieve event (re)
            - update event (ue)
            - delete event (de)
        (Su)pport (U)ser : (SuU)
            + list events (le)
            - create event (ce)
            = retrieve event (re)
            = update event (ue)
            - delete event (de)
        (U)ser (W)ith(o)ut (R)ole : (UWoR)
            - list events (le)
            - create event (ce)
            - retrieve event (re)
            - update event (ue)
            - delete event (de)
        (U)nauthenticated (U)ser : (UU)
            - list events (le)
            - create event (ce)
            - retrieve event (re)
            - update event (ue)
            - delete event (de)
    """
    def setUp(self):
        """Setup
        
        Users:
            - Saler
            - Saler not THROUGH
            - Support
            - Support not THROUGH
            - User Without Role
        
        Client:
            - Client
        Contract:
            - Contract
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

        # Contract
        user = User.objects.get(username='saler')
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        contract_form = {
            'sales_contact': user,
            'client': client,
            'status': True,
            'amount': 10.0,
            'payment_due': d,
        }
        contract = Contract(**contract_form)
        contract.save()

    def test_SaU_le_e(self):
        """Test -> empty list
            Saler User/
                + list events
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 204)

    def test_SaU_le_ne(self):
        """Test -> not empty list
            Saler User/
                + list events
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_ce_th(self):
        """Test
            Saler User/
                THROUGH
                    + create event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        response = self.client.post(path=url, data=event_form)
        self.assertEqual(response.status_code, 201)

    def test_SaU_ce_nth(self):
        """Test
            Saler User/
                not THROUGH
                    - create event
        """
        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        response = self.client.post(path=url, data=event_form)
        self.assertEqual(response.status_code, 403)

    def test_SaU_re_th(self):
        """Test
            Saler User/
                THROUGH
                    + retrieve event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SaU_re_nth(self):
        """Test
            Saler User/
                not THROUGH
                    - retrieve event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='salerNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SaU_ue(self):
        """Test
            Saler User/
                - update event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        event_update = {
            'attendees': 2,
        }
        response = self.client.put(path=url, data=event_update)
        self.assertEqual(response.status_code, 403)

    def test_SaU_de(self):
        """Test
            Saler User/
                - delete event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SuU_le(self):
        """Test
            Support User/
                + list event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SuU_ce(self):
        """Test
            Support User/
                - create event
        """
        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        response = self.client.post(path=url, data=event_form)
        self.assertEqual(response.status_code, 403)

    def test_SuU_re_th(self):
        """Test
            Support User/
                THROUGH
                    + retrieve event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def test_SuU_re_nth(self):
        """Test
            Support User/
                not THROUGH
                    - retrieve event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='supportNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_SuU_ue_th(self):
        """Test
            Support User/
                THROUGH
                    + update event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        event_update = {
            'attendees': 2,
        }
        response = self.client.put(path=url, data=event_update)
        self.assertEqual(response.status_code, 200)

    def test_SuU_ue_nth(self):
        """Test
            Support User/
                not THROUGH
                    - update event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='supportNTH')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        event_update = {
            'attendees': 2,
        }
        response = self.client.put(path=url, data=event_update)
        self.assertEqual(response.status_code, 403)

    def test_SuU_de(self):
        """Test
            Support User/
                - delete event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='support')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_le(self):
        """Test
            User Without Role/
                - events
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_ce(self):
        """Test
            User Without Role/
                - event
        """
        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        response = self.client.post(path=url, data=event_form)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_re(self):
        """Test
            User Without Role/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_ue(self):
        """Test
            User Without Role/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        event_update = {
            'attendees': 2,
        }
        response = self.client.put(path=url, data=event_update)
        self.assertEqual(response.status_code, 403)

    def test_UWoR_de(self):
        """Test
            User Without Role/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        user = User.objects.get(username='user')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 403)

    def test_UU_le(self):
        """Test
            Unauthenticate User/
                - events
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        self.client.logout()
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_ce(self):
        """Test
            Unauthenticate User/
                - event
        """
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        response = self.client.post(path=url, data=event_form)
        self.assertEqual(response.status_code, 401)

    def test_UU_re(self):
        """Test
            Unauthenticate User/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 401)

    def test_UU_ue(self):
        """Test
            Unauthenticate User/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        event_update = {
            'attendees': 2,
        }
        response = self.client.put(path=url, data=event_update)
        self.assertEqual(response.status_code, 401)

    def test_UU_de(self):
        """Test
            Unauthenticate User/
                - event
        """
        user = User.objects.get(username='saler')
        self.client.force_authenticate(user=user)
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/'
        d = datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        event_form = {
            'support_contact': 'support',
            'attendees': 1,
            'event_date': d,
            'notes': 'text test',
        }
        self.client.post(path=url, data=event_form)

        self.client.logout()
        url = 'http://127.0.0.1:8000/client/1/contract/1/event/1/'
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, 401)
