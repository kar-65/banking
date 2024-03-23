from . import views
from django.urls import path,include

urlpatterns = [
    # path('',include('bankAct.urls'))
    path('',views.customer,name='customer'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('customerlog', views.customerlog, name='customerlog'),
    path('exitsite', views.exitsite, name='exitsite'),

]
