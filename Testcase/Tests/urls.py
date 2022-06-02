from django.urls import path
from .views import *

urlpatterns = [
    path('', CardsList.as_view(), name='home'),
    path('<int:card_id>/', CardView.as_view(), name='card'),
    path('delete/<int:pk>',  delete_card, name='delete'),
    path('activate/<int:pk>/', activate_card, name='activate'),
    path('add_card/', AddCard.as_view(), name='add_card'),
    path('history/<int:pk>/', history, name='history'),
    path('reg/', registrate_user, name='regis'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/<int:pk>', change, name='edit'),
]