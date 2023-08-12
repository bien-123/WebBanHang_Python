from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name="detailView"),
    path('', views.index, name="index"),
    path('abc/', views.abc, name="abc"),
    path('list/', views.viewlist, name="list"),
    path('<int:question_id>', views.vote, name="vote")
]
