from django.urls import path
# 1
from pypro.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
            ]
