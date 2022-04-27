from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializer import RegisterSerializer, EmailverificationSerializer, LoginSerializer
from .utils import Util
from .models import User
from django.conf import settings
import jwt


class RegisterView(generics.CreateAPIView):
    "A class to register new users"
    serializer_class = RegisterSerializer

    def post(self, request):
        # serializer = self.serializer_class(data=request.data)
        try:
            user = request.data
            print('USER', user)
            serializer = self.serializer_class(data=user, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            
            # Send Email
            Util.get_data_send_email(user_data, request)
            return Response(user_data, status = status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'error': str(err)}, status = status.HTTP_400_BAD_REQUEST)

class VerifyEmail(views.APIView):
    
    "decodes the token sent to the user to verify the email"
    
    serializer_class = EmailverificationSerializer
    #: this function is triggered when user clicks on the link 
    #: sent to his email2

    def get(self, request):
        token = request.Get['token']
        try:
            #: get secret key from settings
            secret_key = settings.SECRET_KEY

            #: decode the token sent to the user
            payload = jwt.decode(token, secret_key)

            #: identify the user from the token
            user = User.objects.get(id = payload['user_id'])

            #: verify user
            if not user.is_verified():
                user.is_verified = True
                user.save()
            return Response({'email': 'Email successfully activated'}, status= status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Linked expired'}, status = status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({'error': 'Invalid token'}, status = status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data = user)
        serializer.is_valid(raise_exceptions = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


