from django.urls import path
from cride.circles.views import list_circles, create_cricle

urlpatterns = [
    path('circles/', list_circles),
    path('circles/create/', create_cricle),
]