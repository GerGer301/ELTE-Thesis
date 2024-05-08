from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/main/', views.main_page, name='main_page'),
    path('profile/update/', views.profile_update, name='profile_update'),
]
