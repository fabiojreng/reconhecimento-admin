from django.db import models
import uuid
from apps.administrators.models import Administrator
from apps.users.models import User


class Log(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    access_at = models.DateTimeField(auto_now_add=True)
    administrator_id = models.ForeignKey(
        Administrator, null=True, on_delete=models.SET_NULL, related_name="logs"
    )

    def __str__(self):
        return f"{self.log_id} - {self.access_at}"


class RecognitionLog(models.Model):
    recognition_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user_id = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="recognition_logs"
    )
    access_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.recognition_id} - {self.user_id}"
