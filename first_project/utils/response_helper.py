from rest_framework.response import Response
from rest_framework import status

def Ok(data):
    return Response({
                    'data': data,
                    'message':"sucessfull",
                    'code':status.HTTP_200_OK
                }, status=status.HTTP_200_OK)