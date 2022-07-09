from django.urls import path

from .views import CustomPasswordChangeView, MyAccountPageView

urlpatterns = [
    path(
        "password/change/", CustomPasswordChangeView.as_view(),
        name="account_change_password"
    ),
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
]
