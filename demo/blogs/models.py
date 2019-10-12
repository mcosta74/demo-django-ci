from django.db import models

# Create your models here.

class Author(models.Model):
    nickname = models.SlugField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.nickname})'

class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(Author, models.SET_NULL, null=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'[{self.date_time.isoformat()}] {self.title} ({self.author.nickname if self.author else "N/A"})'


class Comment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(Author, models.SET_NULL, null=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'[{self.date_time.isoformat()}] {self.content} ({self.author.nickname if self.author else "N/A"})'
