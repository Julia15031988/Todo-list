from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

    class Meta:
        ordering = ["is_done", "-created"]

    def __str__(self):
        task_tags = self.tags.all()
        tag_names = ", ".join([tag.name for tag in task_tags])
        return f"{self.content}: {tag_names} ({self.is_done})"
