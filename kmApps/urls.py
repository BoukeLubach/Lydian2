from django.urls import path

from .views import introPageView, kmeans_analysis_view

urlpatterns = [
    path('intro/', introPageView, name='intro-page'),
    path('km/', kmeans_analysis_view, name='kmeans-analysis'),
    # path('kmDistillation/', kmDistillationView, name='km-distillation'),
]