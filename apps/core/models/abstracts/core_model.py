from django.db import models
from rest_framework.request import Request


class CoreModel(models.Model):
    """
    Abstract model to track metadata for records.

    Fields:
        add_by (int): Stores the profile ID of the user who created the record.
        add_at (datetime): Automatically stores the date and time when the record is created.
        modify_by (int): Stores the profile ID of the user who last modified the record.
        modify_at (datetime): Automatically stores the date and time when the record is last updated.
    """

    add_by = models.IntegerField()
    add_at = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    modify_by = models.IntegerField()
    modify_at = models.DateTimeField(auto_now=True, verbose_name="Update Date")
    is_active = models.BooleanField(default=True)

    def soft_delete(self, using=None):
        """
        soft delete: to update field is_active=False

        Params:
            using: sepecify db alias to operate
        """
        self.is_active = False
        return super().save(using=using)

    class Meta:
        abstract = True


class OwnershipModel(models.Model):
    """
    Abstract model to track ownership of records.

    Fields:
        owner (int): Stores the profile ID of the user who owns the record.
        on_behalf (int): Stores the profile ID of the user acting on behalf of the owner.
    """

    owner = models.IntegerField()
    on_behalf = models.IntegerField(null=True)

    class Meta:
        abstract = True


class RecordNumberingModel(models.Model):
    """
    Abstract model to track ownership of records.

    Fields:
        owner (int): Stores the profile ID of the user who owns the record.
        on_behalf (int): Stores the profile ID of the user acting on behalf of the owner.
    """

    unique_numbering = models.CharField(100)

    class Meta:
        abstract = True
