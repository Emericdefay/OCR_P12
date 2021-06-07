# Django Rest Framework Libs:
from rest_framework.routers import SimpleRouter
# Locals:
from .views import ContractCRUD


router = SimpleRouter()
router.register(r'', ContractCRUD, basename='contract')

urlpatterns = router.urls
