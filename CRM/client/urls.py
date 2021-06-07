# Django Rest Framework Libs:
from rest_framework.routers import SimpleRouter
# Locals:
from .views import ClientCRUD


router = SimpleRouter()
router.register(r'', ClientCRUD, basename='client')

urlpatterns = router.urls
