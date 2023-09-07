from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150,default="Default Title")
    description = models.CharField(max_length=500,default="Your Default Description")
    completed = models.BooleanField(default=False)

    def __str__ (self):

        return self.title

# Create your models here.
