from django.urls import path
from .views import (
    ReviewListView, ReviewCreateView, ReviewThanksView
)

app_name = 'reviews'
urlpatterns = [
    path("", ReviewListView.as_view(), name="list"),
    path("review/", ReviewCreateView.as_view(), name="review"),
    path('review/thanks/', ReviewThanksView.as_view(), name='thanks'),

]
