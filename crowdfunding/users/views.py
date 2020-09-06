from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, UserProfile
from .serializers import CustomUserSerializer, UserProfileSerializer
# import logging
# logger = logging.getLogger(__name__)


# viewing all list of users
class CustomUserList(APIView):
    def get(self, request):
        # Permissions classes moved here to enable anyone to create an account
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

# Need to refine response for creatign a duplicate user        
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        # TODO later improvement, check to ensure no duplicate user
        # if request == CustomUser.email():
        #     return Response(
        #         status=status.HTTP_409_CONFLICT
        #     )
        # else:
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            Response(
                serializer.errors,
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        return Response(serializer.errors)

# viewing/updating the profile of a specific user
class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        if request.user.is_authenticated:
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )

    # Updating user profile data
    def put(self, request, pk):
        user = self.get_object(pk)
        if request.user != user:
            return Response(
                status=status.HTTP_403_FORBIDDEN
            )
        user_profile = user.profile
        data = request.data
        serializer = UserProfileSerializer(
            instance=user_profile,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )