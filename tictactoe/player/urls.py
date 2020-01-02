from django.urls import path
from .views import home, new_invitation, accept_invitation
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url

urlpatterns = [
    path('home/', home, name="player_home"),
    path('login/', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout/', LogoutView.as_view(), name="player_logout"),
    url(r'new_invitation$', new_invitation, name="player_new_invitation"),
    url(r'accept_invitation/(?P<id>\d+)/$', accept_invitation, name="player_accept_invitation"),
]
