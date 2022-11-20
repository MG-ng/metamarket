from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suche', views.search, name="search"),
    path('inserieren', views.post, name="post"),
    path('unsere-partner', views.post, name="partner"),
]