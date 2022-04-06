from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from help.models import Help
from help.serializers import HelpSerializer


# Create your views here.

class helpListView(APIView):
    def get(self, request, format=None):
        help = Help.objects.all()
        serializer = HelpSerializer(help, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HelpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class helpDetails(APIView):
    def get(self, request, pk, format=None):
        help = Help.objects.filter(subject=pk)
        serializer = HelpSerializer(help, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            help = Help.objects.get(subject=pk)
            serializer = HelpSerializer(help, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Help.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            help = Help.objects.get(subject=pk)
            help.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Help.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
