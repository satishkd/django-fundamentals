from django.urls import path
from .views import home
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('home/', home, name="player_home"),
    path('login/', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout/', LogoutView.as_view(), name="player_logout"),
]
