from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sportbikes/', views.sportbikes_index, name='index'),
    path('sportbikes/<int:bike_id>/', views.sportbikes_detail, name='detail'),
    path('sportbikes/create/', views.SportbikeCreate.as_view(), name='sportbikes_create'),
]