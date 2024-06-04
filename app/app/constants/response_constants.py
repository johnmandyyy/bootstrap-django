from rest_framework.response import Response as __Response
from rest_framework import status as __STATUS


class __Messages:
    
    PERMISSION_DENIED_MESSAGE = "Permission Denied"
    VALID = "ACCEPTED"


PERMMISSION_DENIED = __Response(
    {"details": __Messages.PERMISSION_DENIED_MESSAGE}, __STATUS.HTTP_401_UNAUTHORIZED
)
