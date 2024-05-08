
from django.contrib import admin
from django.urls import path,include
from .views import MyPasswordChangeView
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


    # Dashboards
    path('', include('dashboards.urls')),

    # apps
    path('apps/', include('apps.urls')),

    path(
        "accounts/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),

    # all auth
    path('accounts/', include('allauth.urls')),
    # my account
    path('accounts/', include('myaccount.urls', namespace='myaccount'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
