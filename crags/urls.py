from django.urls import path

from . import views

app_name = 'crags'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('crags/', views.IndexCragView.as_view(), name='crags_index'),
    path('crags/cragForm', views.add_crag_view, name='crag_create'),
    path('crags/<int:pk>/', views.DetailCragView.as_view(), name='crag_detail'),
    path('crags/<int:pk_crag>/routeForm/', views.add_route_view, name='route_create'),
    path('crags/<int:pk_crag>/routes/<int:pk>/', views.IndexRouteView.as_view(), name='route_detail'),
    path('stories/', views.IndexAnecdoteView.as_view(), name='anecdote_index'),
    path('anecdote/<int:pk>/', views.DetailAnecdoteView.as_view(), name='anecdote_detail'),
    path('name_story/<int:pk>/', views.DetailNameStoryView.as_view(), name='name_story_detail'),
    path('crags/<int:pk_crag>/routes/<int:pk_route>/anecdoteForm/', views.add_anecdote_view, name='anecdote_create'),
    path('crags/<int:pk_crag>/routes/<int:pk_route>/nameStoryForm/', views.add_name_story_view, name='name_story_create'),
]
