from django.urls import path
from games.views import (
    GameListView, ContactUsView, GamePlayView, AboutView
)


app_name = 'games'
urlpatterns = [
    path("contact", ContactUsView.as_view(), name="contact"),
    # path('thanks/', GameThanksView.as_view(), name='thanks'),
    path('play/', GamePlayView.as_view(), name='play'),
    path('', GameListView.as_view(), name='list'),
    path('user/<username>/', GameListView.as_view(), name='user'),
    path('about/', AboutView.as_view(), name='about'),
]
