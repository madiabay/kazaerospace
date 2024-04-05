from django.urls import path, include


"""
API urls
"""
urlpatterns = [
    path('', include('users.urls.v1')),
    path('', include('fitness_trainers.urls.v1')),
    # path('', include('schedules.urls.v1')),
    # path('', include('records.urls.v1')),
]
