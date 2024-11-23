from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin


class CoreSerializer(SerializerExtensionsMixin, ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True)

    def create(self, validated_data):
        validated_data["add_by"] = self.request_user.user_id
        validated_data["modify_by"] = self.request_user.user_id
        validated_data["owner"] = self.request_user.user_id
        return super().create(
            validated_data,
        )

    def update(self, instance, validated_data):

        validated_data["modify_by"] = self.request_user.user_id
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        return super().save(**kwargs)

    @property
    def request(self):
        request = self.context.get("request")
        if not request:
            raise AttributeError("Request object not found in serializer context.")

        return request

    @property
    def request_user(self):
        user = getattr(self.request, "user")
        if not user:
            raise AttributeError("user attribute not found in serializer's request.")

        return user

    @property
    def auth(self):
        auth = getattr(self.request, "auth")
        if not auth:
            raise AttributeError("auth attribute not found in serializer's request.")

        return auth
