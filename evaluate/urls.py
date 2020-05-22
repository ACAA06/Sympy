from django.urls import path

from . import views

urlpatterns = [path("", views.contents, name="contents"),
               path("integrate",views.integrate,name="integrate"),
path("derivate",views.differentiate,name="derivate")
               ]
