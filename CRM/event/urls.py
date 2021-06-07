# Django Libs:
from django.urls import path
# Locals:
from .views import EventCRUD


urlpatterns = [
    path("<int:event_id>", EventCRUD),
]
