#from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Lessons
from .forms import LessonForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

# Create your views here.


class AddLesson(LoginRequiredMixin, CreateView):
    template_name = 'lessons/add_lesson.html'
    model = Lessons
    form_class = LessonForm
    success_url = '/lessons'

    @method_decorator(permission_required('lessons.add_lessons', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        try:
            return super().dispatch(*args, **kwargs)
        except PermissionDenied:
            messages.error(self.request, "You don't have permission to access this page.")
            return HttpResponseRedirect('home')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(AddLesson, self).form_valid(form)

class LessonList(ListView):
    '''view all lessons'''
    template_name='lessons/modules.html'
    model = Lessons
    context_object_name='lessons'

class LessonDetail(DetailView):
    '''view a single lesson'''
    template_name='lessons/lesson_detail.html'
    model = Lessons
    context_object_name='lesson'
