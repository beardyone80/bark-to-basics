from django import forms
from .models import Lessons


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = [
            'title',
            'image',
            'image_alt',
            'content',
            'category',
            'status',
            'excerpt',
            ]
                  
        labels = {
            'title': 'Lesson title',
            'image': 'Lesson image',
            'image_alt': 'Describe image',
            'content': 'Lesson content',
            'category': 'Lesson category',
            'status': 'Publish or Draft',
            'excerpt': 'Lesson description',
            }


    def save(self, commit=True):
        instance = super(LessonForm, self).save(commit=False)

        # Prepopulate the slug based on the title
        instance.slug = instance.title.lower().replace(' ', '-')

        if commit:
            instance.save()

        return instance