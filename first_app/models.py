from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=400)
    col1 = models.CharField(max_length=10, default=100)
    def __str__(self):
        return self.name

class Host(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    mem = models.CharField(max_length=100, blank=True, null=True)
    disk = models.CharField(max_length=50, blank=True, null=True)
    cpu = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'host'
    def __str__(self):
        return self.ip