from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Trainer(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    photo = CloudinaryField('image', default='placeholder', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expertise(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    feedback = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name
