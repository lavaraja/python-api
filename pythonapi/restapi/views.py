from django.shortcuts import render
from django.http import HttpResponse,request
import json
import requests
import pandas as pd
from django.http import JsonResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from restapi.models import book
from restapi.serializers import bookSerializer

# Create your views here.
def getBooks(request):
    if request.method == 'GET':
        bookname = request.GET.get('name')

        if not bookname:
            return HttpResponse("Please pass the book name to api to list for the matching books")
        params={"name":bookname}

        ## we can implement redis catching for to recude load on api for repeated requests.

        matching_response=requests.get("https://www.anapioficeandfire.com/api/books",params=params)

        response_data=[]
        if  matching_response.text=="[]":
            response_data=[]
        else:
            org_res_data=pd.io.json.json_normalize(json.loads(matching_response.text))[['name','isbn','authors','numberOfPages','publisher','country','released']]
            response_data=org_res_data.rename(columns={"released":"release_date","numberOfPages":"number_of_pages"}).to_dict()
        response={

            "status_code": 200,
            "status": "success",
            "data": response_data

        }

        return JsonResponse(response)
    else:
        return HttpResponse("Only get method supported on this URL. If you want to add books to local database please use POST http://localhost:8080/api/v1/books")



## own api implementation

@csrf_exempt
def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = book.objects.all()
        serializer = bookSerializer(snippets, many=True)
        response = {

            "status_code": 200,
            "status": "success",
            "data": serializer.data

        }
        return JsonResponse(response, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = bookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {

                "status_code": 200,
                "status": "success",
                "data": serializer.data

            }
            return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def book_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = book.objects.get(pk=pk)
    except book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = bookSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = bookSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)