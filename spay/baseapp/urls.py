from django.urls import path
from .views import home,charge,success

urlpatterns = [
    path('',home,name='home'),
    path('charge/',charge,name='charge'),
    path('success/<str:args>/',success,name='success')
]
