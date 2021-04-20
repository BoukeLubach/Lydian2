from django.urls import path

from .views import introPageView, kmeans_analysis_view, kmDistanceView
from kmApps.dash_apps import kmDistanceApp

urlpatterns = [
    path('intro/', introPageView, name='intro-page'),
    path('km/', kmeans_analysis_view, name='kmeans-analysis'),
    path('kmExample/', kmDistanceView, name='km-distance'),
]