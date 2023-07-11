"""firstsite URL Configuration

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
from firstsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView),

    path('n_step_with_volatility/',views.N_STEP_WITH_VOLATILITY),
    path('n_step_option_price/', views.n_step_option_price),

    path('n_step/',views.N_STEP),
    path('n_step_option_price_without/', views.n_step_option_price_without),

    path('2_step/',views.TWO_STEP),
    path('two_step_option_price_without/', views.two_step_option_price_without),

    path('2_step_with_volatility/',views.two_step_with_volatility),
    path('two_step_option_price/', views.two_step_option_price),

    path ('bs_option/',views.bs_option ),
    path('bs_value/', views.bs_value),

]
