from django.urls import path
from . import views
from .views import IndexClass, LoginClass, ViewUser, view_product

urlpatterns = [
    path('', IndexClass.as_view(), name="index"),
    path('login/', LoginClass.as_view(), name="login"),
    path('user/', ViewUser.as_view(), name="user"),
    path('view-pro/', view_product, name="view-product")
]
