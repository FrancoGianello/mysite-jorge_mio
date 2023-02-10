from django.urls import path, re_path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path("detalle/<int:id>/", views.detalle, name="detalle"),
    path("<int:id>/vote/", views.vote, name="vote"),
    path("<int:id>/resultado/", views.resultado, name="resultado")
]