from django.db import models
from django.conf import settings


class Message(models.Model):
    """
    Main message model. Contains sender info, time of creation and text of message.
    Also contains file field for saving users files.
    """
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files', null=True, blank=True)

    def __unicode__(self):
        return self.text[:30]
