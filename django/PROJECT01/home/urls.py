from django.urls import path
from . import views

urlpatterns = [
    path('static_example', views.static_example),
    path('user_new/',views.user_new),
    path('user_create/',views.user_create),
    path('get/',views.get),
    path('throw/', views.throw),
    path('result/',views.result),
    path('catch/',views.catch),
    path('pong/',views.pong),
    path('ping/',views.ping),
    path('template_example/', views.template_example),
    path('isbirth/',views.isbirth),
    path('area/<int:r>/',views.area),
    path('multiply/<int:a>/<int:b>/',views.multiply),
    path('introduce/<name>/<int:age>/',views.introduce),
    path('cube/<int:num>/',views.cube),
    path('hello/<name>/', views.hello),
    path('dinner/', views.dinner),
    path('lotto/',views.lotto),
    path('midnight/',views.midnight),
    path('midnight2/',views.midnight2),
    path('hola/',views.hola),
    path('index/',views.index),
    path('index2/',views.index2),
    path('',views.home),
]