from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True,max_length=255)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
      