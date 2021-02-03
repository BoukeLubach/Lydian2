from django.urls import path

from .views import introPageView

urlpatterns = [
    path('intro/', introPageView, name='intro-page'),
    # path('kmDistillation/', kmDistillationView, name='km-distillation'),
]