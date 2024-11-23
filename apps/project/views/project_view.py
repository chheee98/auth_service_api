from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from rest_framework import viewsets

from apps.project.models.project import Project
from apps.project.serializers.project_serializer import (
    ProjectListSerializer,
    ProjectSerializer,
)


class ProjectView(SerializerExtensionsAPIViewMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer

        return self.serializer_class

    def get_extensions_mixin_context(self):
        context = super(ProjectView, self).get_extensions_mixin_context()
        context["expand"] = set(
            [
                field_name
                for field_name in context["expand"]
                if field_name != "prevent_expansion"
            ]
        )
        return context

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        project = super().retrieve(request, *args, **kwargs)
        return project
