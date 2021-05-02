"""hms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from checkin import views

from django.conf.urls.static import static # new
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', views.bookingView, name='booking'),
    path('details/', views.display, name='details'),
    path('update/', views.update, name='update'),
    path('update1/', views.update, name='update1'),
    path('delete/', views.delete, name='delete'),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)