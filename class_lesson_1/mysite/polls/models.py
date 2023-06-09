from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    put_date = models.DateTimeField('date published')

    def __str__(self):
        return

class Cgoice