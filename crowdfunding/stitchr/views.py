from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import StitchrSerializer
from django.http import Http404
from rest_framework import status

class StitchrList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = StitchrSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StitchrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class StitchrDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = StitchrSerializer(project)
        return Response(serializer.data)