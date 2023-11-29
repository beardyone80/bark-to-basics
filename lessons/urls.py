from django.urls import path
from .views import AddLesson, LessonList, LessonDetail, edit_comment, delete_comment

urlpatterns = [
    path('', AddLesson.as_view(), name='add_lesson'),
    path('lessons/', LessonList.as_view(), name='modules'),
    path("lessons/<slug:slug>/", LessonDetail.as_view(), name='lesson_detail'),
    path('lessons/<slug:slug>/edit_comment/<int:comment_id>', edit_comment, name='edit_comment'),
    path('lessons/<slug:slug>/delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]
