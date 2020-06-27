from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer

# Create your views here.
class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # Say what to do when there is a post request to our django website through our API
    def post(self, request, *args, **kwargs):
        # Create a serialzer with the data we want to POST
        file_serializer = FileSerializer(data=request.data)

        # A little safe check the POST request is valid or not
        if file_serializer.is_valid():

            # Tell the serializer to save the data to the API, this actually does the HTTP POST request
            file_serializer.save()

            # Return status 201_CREATED if the POST request is success
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        else:
            # Return status 400_BAD_REQUEST if the POST request is fail
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)