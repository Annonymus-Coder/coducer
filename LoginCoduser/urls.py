from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('register/',views.signUp,name='Register'),
    path('login/',views.signIn,name='Login'),
    path('logout/', views.logoutUser, name="logout"),
]