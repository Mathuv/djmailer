from django.shortcuts import render
from django.http.response import JsonResponse

# For DRF
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def hello_world(request):
    return JsonResponse({"message": "hello world!"})

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World DRF!"})
