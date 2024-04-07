from django.urls import path
from schedules import views


urlpatterns = [
    path('schedules/create/', views.ScheduleViewSet.as_view({'post': 'create_schedule'})),
]
