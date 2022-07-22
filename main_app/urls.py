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
    path('sportbikes/<int:sportbike_id>/assoc_colors/<int:colors_id>/', views.assoc_colors, name='assoc_colors'),
    path('colors/', views.ColorsList.as_view(), name='colors_index'),
    path('colors/<int:pk>/', views.ColorsDetail.as_view(), name='colors_detail'),
    path('colors/create/', views.ColorsCreate.as_view(), name='colors_create'),
    path('colors/<int:pk>/update/', views.ColorsUpdate.as_view(), name='colors_update'),
    path('colors/<int:pk>/delete/', views.ColorsDelete.as_view(), name='colors_delete'),
]