from django.urls import path, include


"""
for versions APIs
"""
urlpatterns = [
    path('v1/', include('api_urls.v1')),
]
