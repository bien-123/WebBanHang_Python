from django.urls import path
from . import views
from .views import IndexClass, LoginClass, ViewUser


urlpatterns = [
    path('', IndexClass.as_view(), name="index"),
    path('login/', LoginClass.as_view(), name="login"),
    path('user/', ViewUser.as_view(), name="user"),
]
