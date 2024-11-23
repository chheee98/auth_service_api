from django.db import models
from apps.core.models.abstracts.core_model import CoreModel, OwnershipModel
from django.utils import timezone
from apps.project.models.project import Project


class Milestone(CoreModel, OwnershipModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="milestones"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "project_milestone"
