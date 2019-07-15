from django.urls import path

from . import views

app_name = 'crags'
urlpatterns = [
    path('', views.IndexCragView.as_view(), name='index'),
    path('<int:pk>/', views.DetailCragView.as_view(), name='crag_detail'),
    #path('<int:pk_crag>/<int:pk>/', views.DetailRouteView.as_view(), name='route_detail'),
    path('<int:pk_crag>/<int:pk>/', views.IndexRouteView.as_view(), name='route_index'),
    path('stories/', views.IndexAnecdoteView.as_view(), name='anecdote_index'),
    path('anecdote/<int:pk>/', views.DetailAnecdoteView.as_view(), name='anecdote_detail'),
    path('name_story/<int:pk>/', views.DetailNameStoryView.as_view(), name='name_story_detail'),
    path('crag/<int:pk_crag>/route/<int:pk>/anecdoteForm/', views.CreateAnecdoteView.as_view(), name='anecdote_create'),
]
