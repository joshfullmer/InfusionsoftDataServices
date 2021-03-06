"""infusionsoftdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('slack/', views.slack, name='slack'),
    path('admin/', admin.site.urls),
    path(
        'freetrialtransfer/',
        include('freetrialtransfer.urls', namespace='freetrialtransfer')),
    path('tablequery/', include('tablequery.urls', namespace='tablequery')),
    path(
        'emailhistoryexport/',
        include('emailhistoryexport.urls', namespace='emailhistoryexport')),
    path('code/', views.auth_code, name='auth_code'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
