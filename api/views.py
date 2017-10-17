from django.shortcuts import render
from django.http.response import JsonResponse

# For DRF
from rest_framework.views import APIView
from rest_framework.response import Response

# For function based view
from rest_framework.decorators import api_view

# After adding serializers
from .serializers import HelloWorldSerializer
from .serializers import SubscriberSerializer
from .models import Subscriber


# Create your views here.
def hello_world(request):
    return JsonResponse({"message": "hello world!"})

#function based DRF view
@api_view(["GET","POST"])
def hello_world_function(request):
    if request.method == "GET":
        return Response({"message": "Hello World DRF Function View"})
    else:
        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {} DRF Function View!".format(name)})


# Class based DRF api_view
class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World DRF Class View!"})


    def post(self, request):
        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get("name")
            age = valid_data.get("age")

            return Response({"message": "Hello {}, you're {} years old".format(name, age)})
        else:
            return Response({"errors": serializer.errors})

        name = request.data.get("name")
        if not name:
            return Response({"error": "No name passed"})
        return Response({"message": "Hello {}!".format(name)})


class SubscriberView(APIView):
    def get(self, request):
        all_subscribers = Subscriber.objects.all()
        serialized_subscribers = SubscriberSerializer(all_subscribers, many=True)
        return Response(serialized_subscribers.data)
        # return Response({"message": "Hello World!"})

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber_instance = Subscriber.objects.create(**serializer.data)
            return Response({"message": "Created subscriber {}". format(subscriber_instance.id)})
        else:
            return Response({"errors": serializer.errors})