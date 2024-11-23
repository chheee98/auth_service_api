from rest_framework import routers
from django.urls import include, path
from apps.project.views.project_view import ProjectView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"project", ProjectView, basename="Project")

urlpatterns = [
    path("", include(router.urls)),
    # path(
    #     "more_route_hrere", MoreView.as_view(),
    # ),
]
