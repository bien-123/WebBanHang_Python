from django.urls import path
from . import views
from .views import IndexClass


urlpatterns = [
    path('', IndexClass.as_view(), name="index"),

]
