from rest_framework.routers import DefaultRouter
from users import views


"""
CRUD paths for CustomUser
"""
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = router.urls
