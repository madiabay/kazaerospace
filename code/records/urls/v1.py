from rest_framework.routers import DefaultRouter
from records import views

"""
CRUD paths for Record
"""
router = DefaultRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = router.urls
