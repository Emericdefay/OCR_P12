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
            - Support  not THROUGH
            - User Without Role
        
        Client:
            - Client
        Contract:
            - Contract
        """
        pass
    def test_SaU_le(self):
        """Test
        """
        pass
    def test_SaU_ce(self):
        """Test
        """
        pass
    def test_SaU_re(self):
        """Test
        """
        pass
    def test_SaU_ue(self):
        """Test
        """
        pass
    def test_SaU_de(self):
        """Test
        """
        pass

    def test_SuU_le(self):
        """Test
        """
        pass
    def test_SuU_ce(self):
        """Test
        """
        pass
    def test_SuU_re(self):
        """Test
        """
        pass
    def test_SuU_ue(self):
        """Test
        """
        pass
    def test_SuU_de(self):
        """Test
        """
        pass

    def test_UWoR_le(self):
        """Test
        """
        pass
    def test_UWoR_ce(self):
        """Test
        """
        pass
    def test_UWoR_re(self):
        """Test
        """
        pass
    def test_UWoR_ue(self):
        """Test
        """
        pass
    def test_UWoR_de(self):
        """Test
        """
        pass

    def test_UU_le(self):
        """Test
        """
        pass
    def test_UU_ce(self):
        """Test
        """
        pass
    def test_UU_re(self):
        """Test
        """
        pass
    def test_UU_ue(self):
        """Test
        """
        pass
    def test_UU_de(self):
        """Test
        """
        pass