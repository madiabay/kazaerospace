from rest_framework.routers import DefaultRouter
from fitness_trainers import views


"""
CRUD paths for FitnessTrainers and Halls
"""
router = DefaultRouter()
router.register(r'fitness-trainers', views.FitnessTrainerViewSet)
router.register(r'halls', views.HallViewSet)

urlpatterns = router.urls
