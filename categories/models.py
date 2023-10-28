from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
