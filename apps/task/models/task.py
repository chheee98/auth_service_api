from django.db import models
from apps.core.models.abstracts.core_model import CoreModel, OwnershipModel
from apps.project.models.milestone import Milestone


class Task(CoreModel, OwnershipModel):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("urgent", "Urgent"),
    ]

    STATUS_CHOICES = [
        ("to_do", "To Do"),
        ("in_progress", "In Progress"),
        ("review", "Review"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="medium"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="to_do")
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    due_date = models.DateField(null=True, blank=True)
    milestone = models.ForeignKey(
        Milestone, on_delete=models.CASCADE, related_name="tasks", blank=True
    )

    class Meta:
        db_table = "task_task"
