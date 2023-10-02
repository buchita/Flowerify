"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from projectApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    # links pages
    path('admin/', admin.site.urls),
    path('', include('projectApp.urls')),
    path("flower/daisy/", views.DaisyInformation, name="daisyInformation"),
    path("flower/blanketFlower/", views.BlanketFlower, name="blanketflower"),
    path("flower/buttercup/", views.Buttercup, name="buttercup"),
    path("flower/carnation/", views.Carnation, name="carnation"),
    path("flower/dandelion/", views.Dandelion, name="dandelion"),
    path("flower/cornpoppy/", views.CornPoppy, name="cornpoppy"),
    path("flower/lotus/", views.Lotus, name="lotus"),
    path("flower/marigold/", views.Marigold, name="marigold"),
    path("flower/sunflower/", views.Sunflower, name="sunflower"),
    path("flower/rose/", views.Rose, name="rose"),
    path('flower/upload/', views.upload_file, name="uploader"),
    path('display/', views.filter, name="display"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)