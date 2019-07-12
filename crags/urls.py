from django.urls import path

from . import views

app_name = 'crags'
urlpatterns = [
    path('', views.IndexCragView.as_view(), name='index'),
    path('<int:pk>/', views.DetailCragView.as_view(), name='crag_detail'),
    path('<int:pk_crag>/<int:pk>/', views.DetailRouteView.as_view(), name='route_detail'),
]
