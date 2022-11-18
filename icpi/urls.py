"""icpi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import RedirectView

from hinario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hinos/page=1', views.hinos01, name='hinos01'),
    path('hinos/page=2', views.hinos02, name='hinos02'),
    path('hinos/page=3', views.hinos03, name='hinos03'),
    path('hinos/page=4', views.hinos04, name='hinos04'),
    path('hinos/page=5', views.hinos05, name='hinos05'),
    path('hino/<int:id>/', views.hino, name='hino'),
    path('', RedirectView.as_view(url = '/hinos/page=1')),
]
