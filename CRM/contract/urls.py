# Django Libs:
from django.urls import path
# Locals:
from .views import ContractCRUD


urlpatterns = [
    path("<int:contract_id>", ContractCRUD),
]
