import json
from django.http import JsonResponse
from games.models import Game

from django.views.generic import (
    TemplateView
)


class HomeView(TemplateView):
    template_name = "play/play.html"


class MathGameView(TemplateView):
    template_name = "play/math-game.html"


class AnagramPlayView(TemplateView):
    template_name = "play/anagram-play.html"


def record_score(request):
    data = json.loads(request.body)

    word_length = data["word_length"]

    title = data["game"]
    score = data["score"]

    game_title_id = 'if you see this, then if statement not working'

    if title == Game.Anagram_Hunt:
        game_title_id = 2
    if title == Game.Math_Facts:
        game_title_id = 1

    user_id = request.user.id

    if title == Game.Anagram_Hunt:
        new_score = Game(title=title, score=score, user_id=user_id, word_length=word_length, game_title_id=game_title_id)
        new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)