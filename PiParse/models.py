from django.db import models


class PiPosts(models.Model):
    p_id = models.IntegerField()
    rating = models.IntegerField()
    post_link = models.TextField()
    title = models.TextField()
    timestamp = models.DateTimeField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-rating", ]


class PostContents(models.Model):
    type = models.CharField(max_length=10)
    pre_content = models.TextField(blank=True)
    content = models.TextField()
    post = models.ForeignKey(PiPosts, related_name='contents')

    class Meta:
        ordering = ["id", ]