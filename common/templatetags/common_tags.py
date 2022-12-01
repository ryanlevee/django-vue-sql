from django import template
from django.db.models import Q

from reviews.models import Review
from games.models import Game

register = template.Library()


@register.inclusion_tag('common/game.html')
def angr_leader():

    games_ana = Game.objects.all().filter(game_title_id=2)
    a_by_score = games_ana.order_by('score').reverse()
    a_leader = a_by_score.first()

    return {'game': a_leader}


@register.inclusion_tag('common/game.html')
def math_leader():

    games_mat = Game.objects.all().filter(game_title_id=1)
    m_by_score = games_mat.order_by('score').reverse()
    m_leader = m_by_score.first()

    return {'game': m_leader}


@register.inclusion_tag('common/review.html')
def review_carousel():
    count = Review.objects.count()
    reviews = Review.objects.all()

    return {'reviews': reviews}
