from django.db import models


class signup(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    phno = models.CharField(max_length=16, blank=False, unique=True)
    email = models.CharField(max_length=25, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=15, blank=False)

    class Meta:
        db_table = "signup_table"

class cartitem(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    cost = models.CharField(max_length=10)

    class Meta:
        db_table = "cart_table"







qwertyhujhygfdasQWERTHFGDVZCSAWERTHYGCFDEAWEGFB