from django.urls import path
from .views import AddLesson, LessonList, LessonDetail

urlpatterns = [
    path('', AddLesson.as_view(), name='add_lesson'),
    path('lessons/', LessonList.as_view(), name='modules'),
    path("lessons/<slug:slug>/", LessonDetail.as_view(), name='lesson_detail'),
]