from django.urls import path

from .views import (
    HomeView, MathGameView, AnagramPlayView, record_score
)

app_name = 'play'
urlpatterns = [
    path('', HomeView.as_view(), name='play'),

    # PLAY GAMES
    path('anagram-play/', AnagramPlayView.as_view(), name='anagram-play'),
    # path('math-play/', AnagramPlayView.as_view(), name='math-play'),

    # STAGING
    path('math-game/', MathGameView.as_view(), name='math-game'),

    # RECORD SCORE FUNCTION
    path('record-score/', record_score, name="record-score"),
]
