from django.db import models   #here we will create tables of our project

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    completed = models.BooleanField(default=False) #here fields name,datatye and length

    def __str__(self):
        return self.title   #this will work when an object will call Todo at that time title will be return not necessary to write this 
