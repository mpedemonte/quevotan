from rest_framework.routers import DefaultRouter
from customer.views import CustomerViewSet
 
router = DefaultRouter()
router.register('customers', CustomerViewSet, 'Customer')
urlpatterns = router.urls