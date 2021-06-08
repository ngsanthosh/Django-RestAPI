# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

import json
# Create your views here.

@api_view()
def apiusers(request):
    users=[
        {
            "name":"Santhosh",
            "state":"TamilNadu"
        },
        {
            "name":"Gokul",
            "state":"Telangana"
        }
    ]
    return Response(json.dumps(users))