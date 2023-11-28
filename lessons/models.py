from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField

# Create your models here.

Category = (
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

class Lessons(models.Model):



    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_owner")
    image = ResizedImageField(size=[400, None], quality=75, upload_to='lessons/', force_format='WEBP', blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    category = models.CharField(max_length=100, choices=Category, default='afford')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Category, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The title of this lesson is {self.title}"

    class Meta:
        ordering = ["-created_on"]