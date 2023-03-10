from django.db import models

# Create your models here.


class Log(models.Model):
    user_id = models.BigIntegerField()
    messages = models.JSONField(default={'state': 0})


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=15, null=True)
    menu = models.IntegerField(null=True, default=0)

