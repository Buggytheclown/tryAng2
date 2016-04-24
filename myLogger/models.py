from django.db import models


# Create your models here.
class myLoggerGroup(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.TextField()

    class Meta:
        ordering = ["-id", ]


class myLogger(models.Model):
    group = models.ForeignKey(myLoggerGroup, related_name='logs')
    type = models.CharField(max_length=20)
    message = models.TextField()
    error = models.TextField(blank=True)

    def __str__(self):
        return self.type + ': ' + self.message

    class Meta:
        ordering = ["id", ]
