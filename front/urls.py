from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^coucou$' , views.acceuil , name='home'),
    url(r'^accueil$', views.acceuil, name="home"),
    url(r'^coordonnees$' , views.coordonnees , name='coord'),
    #url(r'^coordonnees/$' , views.coordonnees , name='coord'),
]
