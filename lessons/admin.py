from django.contrib import admin
from .models import Lessons

# Register your models here.
@admin.register(Lessons)

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'image',
        'image_alt',
        'content',
        'category',
        'created_on',
        'status',
        'excerpt',
        'updated_on',
    )
    list_filter=('category',)