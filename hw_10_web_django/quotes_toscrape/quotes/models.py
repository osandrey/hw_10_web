from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=1200)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})



class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})

    @classmethod
    def get_top_ten_tags(cls):
        top_tags = cls.objects.annotate(num_quotes=models.Count('quote')).order_by('-num_quotes')[:10]
        return top_tags



class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})