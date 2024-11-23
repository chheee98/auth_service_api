from drf_yasg.utils import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from apps.project.models.project import Project
from drf_writable_nested.serializers import WritableNestedModelSerializer
from apps.project.serializers.milestone_serializer import MileStoneSerializer
from apps.core.serializers.core_serializer import CoreSerializer

class ProjectListSerializer(CoreSerializer):

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "status",
        ]

class ProjectSerializer(WritableNestedModelSerializer, CoreSerializer):
    milestones = MileStoneSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "start_date",
            "status",
            "milestones",
        ]
