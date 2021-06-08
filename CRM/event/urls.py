# Django Rest Framework Libs:
from rest_framework.routers import SimpleRouter
# Locals:
from .views import EventCRUD


router = SimpleRouter()
router.register(r'', EventCRUD, basename='event')

urlpatterns = router.urls
