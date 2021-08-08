from rest_framework.views import exception_handler
from .business_exception import BusinessException
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if not response:
        response = Response(data={})

        if isinstance(exc, BusinessException):
            response.status_code = status.HTTP_400_BAD_REQUEST
            response.data['message'] = str(exc)
            response.data['code'] = 400

        else:
            response.status_code = 400
            response.data['message'] = 'An error occurred on the server, please try again!'
            response.data['code'] = 400
    
    if response.status_code == 400:
        response.data['message'] = 'An error occurred on the server, please try again!'
        response.data['code'] = 400
    else:
        response.data['message'] = str(exc)
        response.data['code'] = response.status_code
    
    return response