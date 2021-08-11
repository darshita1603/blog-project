from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns=[
    path('register/',views.register,name="register-page"),
    path('profile/',views.profile,name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
]
 