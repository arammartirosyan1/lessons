from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:language_id>/language', views.language, name='language'),

]
