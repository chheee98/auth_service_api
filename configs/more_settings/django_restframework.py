REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "EXCEPTION_HANDLER": "configs.exceptions.handler.custom_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication",
    ),
}
