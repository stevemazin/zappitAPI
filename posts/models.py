from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-timestamp']

    def __str__ (self):
        return self.title

class Vote (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
