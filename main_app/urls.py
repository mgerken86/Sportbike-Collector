from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sportbikes/', views.sportbikes_index, name='index'),
    path('sportbikes/<int:sportbike_id>/', views.sportbikes_detail, name='detail'),
    path('sportbikes/create/', views.SportbikeCreate.as_view(), name='sportbikes_create'),
    path('sportbikes/<int:pk>/update/', views.SportbikeUpdate.as_view(), name='sportbikes_update'),
    path('sportbikes/<int:pk>/delete/', views.SportbikeDelete.as_view(), name='sportbikes_delete'),
    path('sportbikes/<int:sportbike_id>/add_photo/', views.add_photo, name='add_photo'),
    path('sportbikes/<int:sportbike_id>/add_trim/', views.add_trim, name='add_trim'),
]