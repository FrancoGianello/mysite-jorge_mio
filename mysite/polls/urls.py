from django.urls import path, re_path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index.as_view(template_name='polls/index.html'), name='index'),
    path("detalle/<int:pk>/", views.detalle.as_view(template_name="polls/detalle.html"), name="detalle"),
    path("<int:pk>/vote/", views.vote, name="vote"),
    path("<int:pk>/resultado/", views.resultado.as_view(template_name = "polls/resultado.html"), name="resultado")
]