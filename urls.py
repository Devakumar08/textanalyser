from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("left",views.left,name="left"),
    path("right",views.right,name="right"),
    path("main",views.main,name="main"),
    path("analyze",views.analyze,name="analyze"),
    ]