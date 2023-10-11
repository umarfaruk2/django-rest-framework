from django.urls import path
from . import views

urlpatterns = [
    path('studentapiview/', views.api_view, name='studentapi'),

    path('studentapiview/<int:pk>', views.api_view, name='studentapi'),
]