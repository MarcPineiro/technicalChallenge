from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from .utils import handle_error

@api_view(['GET'])
def get_user(request, user_id):
    """
    Retrieve user information by user ID.

    :param request: Request object
    :param user_id: ID of the user to retrieve
    :return: JSON representation of the user
    :raises: 404 Not Found if the user doesn't exist and 500 internal server error for other exceptions
    """
    try:
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    except CustomUser.DoesNotExist as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #return Response("Unhandled error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_user(request):
    """
    Create a new user.

    :param request: Request object containing user data
    :return: JSON representation of the created user
    :raises: 400 Bad Request if data is invalid and 500 internal server error for other exceptions
    """
    try:
        json=request.data
        serializer = CustomUserSerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #return Response("Unhandled error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
