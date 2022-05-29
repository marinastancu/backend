from django.db import models


class Drawing(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    votes = models.IntegerField(blank=True, null=True)
    # upload = models.ImageField()
