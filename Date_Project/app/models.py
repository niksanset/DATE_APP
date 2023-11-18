from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Human(models.Model):
    first_name_user = models.CharField(max_length=255)
    last_name_user = models.CharField(max_length=255)
    login_user = models.CharField(max_length=255)
    password_user = models.CharField(max_length=255)
    age_user = models.PositiveIntegerField()
    about_user = models.CharField(max_length=255)
    hobby_user = models.CharField(max_length=255)
    music_user = models.CharField(max_length=255)
    films_user = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            blank=True,
                            unique=True)
    
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f"{self.first_name_user}-{self.last_name_user}")
        return super().save()
    
    


    def __str__(self):
        return f"{self.first_name_user} - {self.last_name_user}"
