from configs.env import env

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": env.str('OAUTH_GOOGLE_CLIENT_ID'),
            "secret": env.str('OAUTH_GOOGLE_SECRET'),
            "key": env.str('OAUTH_GOOGLE_KEY'),
        },
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
