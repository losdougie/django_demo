from django.db import models

# Create your models here.
class ToDoType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    priority = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    type = models.ForeignKey(ToDoType, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=255)
    # associated_files = models.FileField(upload_to='files/')
    working = models.BooleanField(default=False)

    def __str__(self):
        return self.title


