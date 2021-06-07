# Django Libs:
from django.urls import path
# Locals:
from .views import ClientCRUD


urlpatterns = [
    path("<int:client_id>", ClientCRUD),
]
