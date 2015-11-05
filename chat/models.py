from django.db import models
from django.conf import settings


class Message(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.text[:30]
