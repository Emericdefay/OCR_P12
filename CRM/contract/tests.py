# Django Libs:
from django.contrib.auth.models import User
# Django Rest Framework Libs:
from rest_framework.test import APITestCase
# Locals:
from client.models import Client
from contract.models import Contract
from user.models import (Saler,
                         SalerTHROUGH,
                         Support,
                         SupportTHROUGH)


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
        pass

    def test_SaU_lc(self):
        """Test
        """
        pass
    def test_SaU_cc(self):
        """Test
        """
        pass
    def test_SaU_rc(self):
        """Test
        """
        pass
    def test_SaU_uc(self):
        """Test
        """
        pass
    def test_SaU_dc(self):
        """Test
        """
        pass

    def test_SuU_lc(self):
        """Test
        """
        pass
    def test_SuU_cc(self):
        """Test
        """
        pass
    def test_SuU_rc(self):
        """Test
        """
        pass
    def test_SuU_uc(self):
        """Test
        """
        pass
    def test_SuU_dc(self):
        """Test
        """
        pass

    def test_UWoR_lc(self):
        """Test
        """
        pass
    def test_UWoR_cc(self):
        """Test
        """
        pass
    def test_UWoR_rc(self):
        """Test
        """
        pass
    def test_UWoR_uc(self):
        """Test
        """
        pass
    def test_UWoR_dc(self):
        """Test
        """
        pass

    def test_UU_lc(self):
        """Test
        """
        pass
    def test_UU_cc(self):
        """Test
        """
        pass
    def test_UU_rc(self):
        """Test
        """
        pass
    def test_UU_uc(self):
        """Test
        """
        pass
    def test_UU_dc(self):
        """Test
        """
        pass