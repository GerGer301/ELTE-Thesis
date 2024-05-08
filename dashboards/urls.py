from django.urls import path
from dashboards.views import(
    dashboard,
    main_page
    
)

app_name ='dashboards'


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('main/', main_page, name='main_page'),
]
