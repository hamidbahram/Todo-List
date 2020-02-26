from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100) 

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return "{}".format(self.name)

class Task(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    name_file   = models.FileField(upload_to='uploads/%Y/%m/%d/')
    create      = models.DateTimeField(auto_now_add=True, auto_now=False)
    update      = models.DateTimeField(auto_now_add=False, auto_now=True)
    due_date    = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-create"] 

    def __str__(self):
        return "{}".format(self.title )
   
class File(models.Model):
    name_file = models.ForeignKey(Task, on_delete=models.CASCADE) 

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

    def __str__(self):
        return "{}".format(self.name_file) 