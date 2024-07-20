from django.shortcuts import render

from django.http import JsonResponse

def api_endpoint_1(request):
    data = {"message": "This is a personal Portfolio website"}
    return JsonResponse(data)

def api_endpoint_2(request):
    data = {"message": "Here you will know more about Mohit Ahuja"}
    return JsonResponse(data)
