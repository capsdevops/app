from django.urls import path

from . import views

app_name = "denuncia"

urlpatterns = [
    path("", views.denuncia, name="denuncia"),

]

