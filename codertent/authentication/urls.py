from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('auth/', views.register, name='auth'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login')
]
