from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)
    block_reason = models.TextField(blank=True, null=True)
    photo_url = models.CharField(max_length=1024, null=True, blank=True)
