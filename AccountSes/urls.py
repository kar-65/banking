from . import views
from django.urls import path,include

urlpatterns = [
    path('deposit', views.deposit, name='deposit'),
    path('withdrawal', views.withdrawal, name='withdrawal'),
    path('balance', views.balance, name='balance'),
    path('logout', views.logout, name='logout'),

]
