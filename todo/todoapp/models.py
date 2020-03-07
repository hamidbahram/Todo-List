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


class File(models.Model):
    name_files = models.FileField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        verbose_name = ("File")
        verbose_name_plural = ("Files")

    def __str__(self):
        return "{}".format(self.name_files)


class Task(models.Model):
    TODO  = 1
    DOING = 2
    DONE  = 3

    types = (
        (TODO, 'todo'),
        (DOING, 'doing'),
        (DONE, 'done'),
    )

    title       = models.CharField(max_length=100)
    content     = models.TextField()
    create      = models.DateTimeField(auto_now_add=True, auto_now=False)
    update      = models.DateTimeField(auto_now_add=False, auto_now=True)
    due_date    = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_file   = models.ForeignKey(File, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status_type = models.SmallIntegerField(choices=types)

    class Meta:
        ordering = ["-create"]

    def __str__(self):
        return "{}".format(self.title)
