from apps.project.models.project import Project
from drf_writable_nested.serializers import WritableNestedModelSerializer
from apps.core.serializers.core_serializer import CoreSerializer
from apps.task.models.task import Task


class TaskSerializer(WritableNestedModelSerializer, CoreSerializer):

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "priority",
            "status",
            "progress",
            "due_date",
        ]
