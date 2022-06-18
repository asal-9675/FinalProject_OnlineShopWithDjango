from django.urls import path
from .views import LogoutView
from . import views


app_name = 'accounts'

urlpatterns = [
    
    path('logout/',LogoutView,name = 'logout'),
    path('signup/',views.signup, name='signup'),
]


