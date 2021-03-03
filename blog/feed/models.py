from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(User,
                               related_name="post_author",
                               on_delete=models.SET("Anonymous"),
                               default="12345")
    publishing_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_update_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=3000, editable=True)
    is_published = models.BooleanField(editable=True)
    title = models.CharField(max_length=100, editable=True)
    photo = models.ImageField(null=True, blank=True)

    def author_status(self):
        return self.author.is_authenticated

    def unpublish(self):
        self.is_published = False
        return self.is_published

    def republish(self):
        self.is_published = True
        return self.is_published

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(User,
                               related_name="comment_author",
                               on_delete=models.SET("Anonymous"),
                            default=9876)
    post = models.ForeignKey(Post,
                             related_name="commented_post",
                             on_delete=models.CASCADE,
                             default="101010")
    publishing_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_update_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500, editable=True)
    is_published = models.BooleanField(editable=True)
    photo = models.ImageField(null=True, blank=True)


    def author_status(self):
        return self.author.is_authenticated 

    def unpublish(self):
        self.is_published = False
        return self.is_published

    def republish(self):
        self.is_published = True
        return self.is_published
