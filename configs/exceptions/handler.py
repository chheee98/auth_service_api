import traceback
from django.conf import settings
from django.core.exceptions import (
    ValidationError as DjangoValidationError,
    PermissionDenied,
)
from django.http import Http404
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import exception_handler
from rest_framework import exceptions as rest_framework_exceptions
from rest_framework.serializers import as_serializer_error
from rest_framework.response import Response
from apps.core.exceptions.exception import CoreException


def custom_exception_handler(exc, ctx):
    error_data = {
        "message": [],
        "error": {},
        "errors": [],
    }
    if settings.DEBUG:
        error_data["stack_trace"] = traceback.format_exc().splitlines()

    if isinstance(exc, DjangoValidationError):
        exc = rest_framework_exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = rest_framework_exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = rest_framework_exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    if response is None:
        if issubclass(exc.__class__, CoreException):
            handle_core_exception_error(error_data, exc)
            return Response(error_data, status=exc.status_code)

        handle_unknown_error(error_data, exc)
        return Response(error_data, status=500)

    if isinstance(exc, rest_framework_exceptions.ValidationError):
        handle_validation_exception_error(error_data, exc)
        return Response(
            error_data,
            status=exc.status_code,
            headers=response.headers,
        )

    elif issubclass(exc.__class__, AuthenticationFailed):
        handle_authentication_failed_error(error_data, exc)
        return Response(
            error_data,
            status=exc.status_code,
            headers=response.headers,
        )

    handle_default_exception_error(error_data, exc)
    return Response(
        error_data,
        status=exc.status_code,
        headers=response.headers,
    )


def handle_core_exception_error(error_data, exc):
    _handle_error(error_data, exc.extra)
    error_data["message"].append(exc.message)


def handle_unknown_error(error_data, exc: Exception):
    if settings.DEBUG:
        error_data["message"].extend(
            [getattr(exc, "message", "unknown error"), str(exc)]
        )

    else:
        error_data["message"].append("unknown error")


def handle_validation_exception_error(
    error_data, exc: rest_framework_exceptions.ValidationError
):
    error_data["message"].append("validation error")
    _handle_error(error_data, exc.detail)


def handle_default_exception_error(error_data, exc):
    error_data["message"].append("server error")
    _handle_error(error_data, exc.detail)


def handle_authentication_failed_error(error_data, exc):
    _handle_error(error_data, exc.detail)
    message = getattr(exc.detail, "detail", None) or "authentication failed"
    error_data["message"].append(message)


def get_list_error(error):
    list_dict = [err for err in error if isinstance(err, dict)]
    list_str = [err for err in error if isinstance(err, str)]
    return list_dict, list_str


def _handle_error(error_data, error):
    if isinstance(error, dict):
        error_data["error"] = error

    elif isinstance(error, (list, tuple)):
        list_error_dict, list_error_str = get_list_error(error)
        error_data["errors"] = list_error_dict
        error_data["message"].extend(list_error_str)

    elif isinstance(error, str):
        error_data["message"].append(error)
