from django.contrib import admin
from django.urls import path
from . import views

app_name='boards'

urlpatterns = [
    path("delete/<int:board_pk>/", views.delete, name='delete'),
    path("update/<int:board_pk>/", views.update, name='update'),
    path("detail/<int:board_pk>/", views.detail, name='detail'),
    path("select_food/", views.select_food, name='select_food'),
    path('user_data/',views.user_data, name='user_data'),
    path("new/",views.create, name='create'),
    path("", views.index, name='index'),
]
