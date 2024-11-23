class CoreException(Exception):
    def __init__(self, message, extra=None, status_code=500):
        if not isinstance(message, str):
            raise TypeError(
                f"CoreException:: Expected 'message' to be a str, but got {type(message).__name__}"
            )

        super().__init__(message)

        self.message = message
        self.extra = extra or {}


class BadException(CoreException):
    def __init__(self, message, extra=None):
        super().__init__(message, extra=extra, status_code=400)
