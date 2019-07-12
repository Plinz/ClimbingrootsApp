from django.urls import path

from . import views

app_name = 'stories'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('anecdote/<int:pk>/', views.DetailAnecdoteView.as_view(), name='anecdote_detail'),
    path('name_story/<int:pk>/', views.DetailNameStoryView.as_view(), name='name_story_detail'),
]
