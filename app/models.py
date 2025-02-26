from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    # user = 