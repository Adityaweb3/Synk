from . import views
from django.urls import path

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', views.user_login , name='login'),
    path('' , views.index , name ='index') , 
    path('logout/', auth_view.LogoutView.as_view(http_method_names=["post", "get", "options"], template_name='users/logout.html') , name='logout'),
]