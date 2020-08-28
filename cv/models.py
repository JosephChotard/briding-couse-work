from django.db import models

from ckeditor.fields import RichTextField


class Cv(models.Model):
    content = RichTextField()
