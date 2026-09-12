from django.urls import path
from Hello import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path('Signup/',views.Signup_view,name="Signup"),
    path('Signin/',views.Signin_view,name='Signin'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')
]
