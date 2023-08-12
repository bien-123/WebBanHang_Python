from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name="detailView"),
    path('', views.index, name="index"),
    path('abc/', views.abc, name="abc"),
    path('list/', views.viewlist, name="list")
]
