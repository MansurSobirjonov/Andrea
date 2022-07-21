from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.CharField(max_length=222)
    message = models.TextField()

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.email)
