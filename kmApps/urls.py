from django.urls import path
from .dash_apps import kmDistillation
from .views import kmDistillationView

urlpatterns = [
    path('kmDistillation/', kmDistillationView, name='km-distillation'),
]