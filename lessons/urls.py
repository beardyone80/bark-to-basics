from django.urls import path
from .views import AddLesson, LessonList, LessonDetail

urlpatterns = [
    path('', AddLesson.as_view(), name='add_lesson'),
    path('lessons/', LessonList.as_view(), name='modules'),
    path("lessons/<slug:slug>/", LessonDetail.as_view(), name='lesson_detail'),
    path('lessons/<slug:slug>/edit_comment/<int:comment_id>/', LessonDetail.as_view(), name='edit_comment'),
    path('lessons/<slug:slug>/delete_comment/<int:comment_id>/', LessonDetail.as_view(), name='delete_comment'),
]