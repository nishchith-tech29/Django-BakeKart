from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug=models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,max_length=255)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
