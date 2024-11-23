from django.db import models
from apps.core.models.abstracts.core_model import CoreModel, OwnershipModel
from django.utils import timezone


class Project(CoreModel, OwnershipModel):
    STATUS_CHOICES = [
        ("received", "Received"),
        ("in_progress", "In Progress"),
        ("on_hold", "On Hold"),
        ("completed", "Completed"),
    ]

    # client = models.ForeignKey(
    #     Client, on_delete=models.CASCADE, related_name="projects"
    # )
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now().date())
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="received")

    class Meta:
        db_table = "project_project"
