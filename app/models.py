from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    # cat_choices = [("high", "high"),("medium", "medium"),("low", "low"),]
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Todolist(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="Status", default=False, null=True, blank=True)
    
    class Meta:
        ordering = ['-created']
    
