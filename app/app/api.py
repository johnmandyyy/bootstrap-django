from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from app.helpers import authentication

class Login(APIView):

    def post(self, request, *args, **kwargs):
        try:

            un = request.data['username']
            pw = request.data['password']

            user = authenticate(request, username=un, password=pw)
            login(request, user)

            if user is not None:

                token = authentication.Token()
                token = token.generate_token(request)
                login(request, user)  # Library level not instance.

                return Response({
                    "details": "Login Successful",
                    "token": token
                }, 200)
            
        except Exception as e:
            return Response({
                "details": "Invalid Credentials"
            }, 401)