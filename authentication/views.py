from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import RegisterSerializer
from .utils import Util


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

class VerifyEmail(generics.GenericAPIView):
    "verifies user email"
    def get(self):
        pass
