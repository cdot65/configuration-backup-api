from django.db import models


class Golden(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=100, blank=True, default='')
    golden = models.TextField(blank=True)
    diff = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='configs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
