from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default=1)
    
    
    def __str__(self):
        return self.title
        