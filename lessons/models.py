from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.utils.text import slugify

# Create your models here.

CATEGORY = (
    ('afford', 'Afford'),
    ('time', 'Time'),
    ('needs', 'Time'),
    ('feed', 'Feed'),
    ('sleep', 'Sleep'),
    ('grooming', 'Grooming'),
    ('exercise', 'Exercise'),
    ('behaviour', 'Behaviour'),
    ('healthcare', 'Healthcare'),

)

STATUS = ((0, "Draft"), (1, "Published"))


class Lessons(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="lesson_owner")
    image = ResizedImageField(size=[400, None], quality=75, upload_to='lessons/', force_format='WEBP', blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY, default='afford')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"The title of this lesson is {self.title}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.commenter.username} on Lesson '{self.lesson.title}'"