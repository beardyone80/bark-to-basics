from django.urls import path
from .views import AddLesson

urlpatterns = [
    path('', AddLesson.as_view(), name='add_lesson'),
]