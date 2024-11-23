from drf_writable_nested.serializers import WritableNestedModelSerializer
from apps.project.models.milestone import Milestone
from apps.core.serializers.core_serializer import CoreSerializer
from apps.task.serializers.task_serializer import TaskSerializer


class MileStoneSerializer(WritableNestedModelSerializer, CoreSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Milestone
        fields = [
            "name",
            "description",
            "due_date",
            "status",
            "budget",
            "tasks",
        ]
