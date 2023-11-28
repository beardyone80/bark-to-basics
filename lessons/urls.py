from django.urls import path
from .views import AddLesson, LessonList

urlpatterns = [
    path('', AddLesson.as_view(), name='add_lesson'),
    path('lessons/', LessonList.as_view(), name='modules'),
]