from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class NoticeModel(models.Model):
    title = models.CharField(max_length=22)

    def __str__(self):
        return self.title
