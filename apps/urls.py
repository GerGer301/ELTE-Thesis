from django.urls import path
from apps.views import(
    dynamic_template_apps_view,
    dynamic_template_apps_calendar_view,
    ticket_list,
    ticket_add,
    ticket_edit,
    ticket_delete,
    main_page,
    display_historical_lottery,
    check_lottery
)

app_name ='apps'


urlpatterns = [
    path('<str:template_name>/', dynamic_template_apps_view, name='dynamic_template_apps'),
    path('calendar/<str:template_name>/', dynamic_template_apps_calendar_view, name='dynamic_template_apps_calendar'),
    path('lotterytracker/ticket_list/', ticket_list, name='ticket_list'),
    path('lotterytracker/ticket_list/<str:order_by>/', ticket_list, name='ticket_list'),
    path('lotterytracker/ticket_add/', ticket_add, name='ticket_add'),
    path('lotterytracker/ticket_edit/<int:ticket_id>/', ticket_edit, name='ticket_edit'),
    path('lotterytracker/ticket_delete/<int:ticket_id>/', ticket_delete, name='ticket_delete'),
    path('lotterytracker/main/', main_page, name='main_page'),
    path('lotterytracker/his_list/', display_historical_lottery, name='display_historical_lottery'),
    path('lotterytracker/check_lottery/', check_lottery, name='check_lottery')
]