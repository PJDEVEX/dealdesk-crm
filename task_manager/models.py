from django.db import models
from django.contrib.auth.models import User


def get_salesman():
    """
    Get the default ID for the salesman.
    """
    return 2


STATUS_CHOICES = [
    ("TBD", "Not Started"),
    ("IPG", "In Progress"),
    ("D", "Done"),
]

PRIORITY_CHOICES = [
    ("LP", "Low Priority"),
    ("MP", "Medium Priority"),
    ("TP", "Top Priority"),
]


class TaskManager(models.Model):
    """
    Represents a task manager model.
    """
    title = models.CharField(max_length=55, null=False)
    description = models.CharField(max_length=255)
    due_date = models.DateField(null=False)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Not Started",
        null=False
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default="Medium Priority",
        null=False
    )
    assigned_to = models.ForeignKey(
        'team.Sar',
        on_delete=models.SET(get_salesman),
        related_name='tasks'
    )

    class Meta:
        """
        Meta options for the TaskManager model.
        """
        ordering = ['due_date']

    def __str__(self):
        return self.title
