from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registerUser, name='registerUser'),
    path('login/', views.loginUser, name='signin'),
    path('logout/', views.logoutUser, name='signout'),
    path('forget/', views.forgetPassword, name='forget_password')

]
