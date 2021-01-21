from .views import LoginUser,RegisterUser,Logout
from django.conf import settings
from django.urls.conf import path

app_name = "account"

urlpatterns = [
    path('',RegisterUser.as_view(),name="get_user"),
    path('login', LoginUser.as_view(), name="login_user"),
    path('logout', Logout.as_view(), name="logout_user"),
    path('register', RegisterUser.as_view(), name="register_user"),
]