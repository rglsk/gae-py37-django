from django.db import models


class Task(models.Model):
    COMPLETED = 'co'
    DELETED = 'de'
    IN_PROGRESS = 'ip'
    STATUS_CHOICES = (
        (COMPLETED, 'Completed'),
        (DELETED, 'Deleted'),
        (IN_PROGRESS, 'In progress'),
    )

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=124)
    description = models.CharField(max_length=250)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=IN_PROGRESS,
    )


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    task = models.ForeignKey('Task', related_name='comments', on_delete=models.CASCADE)
