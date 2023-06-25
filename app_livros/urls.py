from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("add_movimentacao/", views.add_movimentacao, name="add_movimentacao")
]
