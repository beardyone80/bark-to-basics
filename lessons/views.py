#from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Lessons
from .forms import LessonForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class AddLesson(LoginRequiredMixin, CreateView):
    template_name = 'lessons/add_lesson.html'
    model = Lessons
    form_class = LessonForm
    success_url = '/lessons'

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(AddLesson, self).form_valid(form)

class LessonList(ListView):
    template_name='lessons/modules.html'
    model = Lessons
    context_object_name='lessons'