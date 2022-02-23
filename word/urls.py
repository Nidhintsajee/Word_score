from django.urls import path
from . import views


urlpatterns = [
    path('add_word/', views.add_word,name='add_word'),
    path('list_scores/', views.list_scores,name='list_scores'),
]
