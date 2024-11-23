from datetime import timedelta
import os
from configs.env import env

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=env.int("JWT_ACCESS_TOKEN_LIFETIME")),
    "REFRESH_TOKEN_LIFETIME": timedelta(seconds=env.int("JWT_REFRESH_TOKEN_LIFETIME")),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ACCESS_COOKIE": env.str("JWT_ACCESS_COOKIE"),
    "REFRESH_COOKIE": env.str("JWT_REFRESH_COOKIE"),
    "REFRESH_EXPIRE": env.str("JWT_REFRESH_COOKIE"),
    "COOKIE_SECURE": env.bool("JWT_COOKIE_SECURE"),
    "COOKIE_HTTP_ONLY": env.bool("JWT_COOKIE_HTTP_ONLY"),
    "COOKIE_SAMESITE": env.str("JWT_COOKIE_SAMESITE"),
    "COOKIE_DOMAIN": env.str("JWT_COOKIE_DOMAIN"),
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_OBTAIN_SERIALIZER": "apps.oauth.serializers.jwt_serializer.TokenPairSerializer",
}

JWT_SIGNING_KEY_PATH = env("JWT_SIGNING_KEY_PATH")
JWT_VERIFYING_KEY_PATH = env("JWT_VERIFYING_KEY_PATH")

if os.path.exists(JWT_SIGNING_KEY_PATH) and os.path.exists(JWT_VERIFYING_KEY_PATH):
    SIMPLE_JWT["ALGORITHM"] = "RS256"
    SIMPLE_JWT["SIGNING_KEY"] = open(JWT_SIGNING_KEY_PATH).read()
    SIMPLE_JWT["VERIFYING_KEY"] = open(JWT_VERIFYING_KEY_PATH).read()
