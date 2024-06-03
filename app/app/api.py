from rest_framework.views import APIView
from rest_framework.response import Response
class TestAPI(APIView):

    def get(self, request):
        if request.user.is_authenticated == True:
            return Response({"message":"Logged IN!"})
        return Response({"message":"NOT Logged IN!"})