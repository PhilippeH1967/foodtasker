"""foodtasker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from foodtaskerapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restaurant/sign-in/', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'),
         name='restaurant-sign-in'),
    path('restaurant/sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='restaurant-sign-out'),
    path('restaurant/', views.restaurant_home, name='restaurant-home'),
    path('restaurant/sign-up/', views.restaurant_sign_up,
         name='restaurant-sign-up'),
    # video
    path('restaurant/account/', views.restaurant_account,name='restaurant-account'),
    path('restaurant/meal/', views.restaurant_meal,name='restaurant-meal'),
    path('restaurant/order/', views.restaurant_order,name='restaurant-order'),
    path('restaurant/report/', views.restaurant_report,name='restaurant-report'),

    # Facebook cours numero 13 - signin and sign up
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token/ (sign in / sign up)
    # /revoke-token (sign out)

    # static est utile pour le chargement de fichier media dans la page sign_up cours 8
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
