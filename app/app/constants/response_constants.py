from rest_framework.response import Response as __Response
from rest_framework import status as __STATUS

PERMMISSION_DENIED = __Response(
    {"details": "Permission Denied"}, __STATUS.HTTP_401_UNAUTHORIZED
)
