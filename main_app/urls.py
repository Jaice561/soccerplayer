from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/<int:player_id>/', views.players_detail, name='detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
    path('players/<int:player_id>/add_training/', views.add_training, name='add_training'),
    path('players/<int:player_id>/assoc_coach/<int:coach_id>/', views.assoc_coach, name='assoc_coach'),
    path('coaches/', views.CoachList.as_view(), name='coaches_index'),
    path('coaches/<int:pk>/', views.CoachDetail.as_view(), name='coaches_detail'),
    path('coaches/create/', views.CoachCreate.as_view(), name='coaches_create'),
    path('coaches/<int:pk>/update/', views.CoachUpdate.as_view(), name='coaches_update'),
    path('coaches/<int:pk>/delete/', views.CoachDelete.as_view(), name='coaches_delete'),
    path('accounts/signup/', views.signup, name='signup')
]
