from django.shortcuts import render
from django.http import HttpResponse,request
import json
import requests
import pandas as pd
from django.http import JsonResponse
# Create your views here.
def getBooks(request):
    if request.method == 'GET':
        bookname = request.GET.get('name')

        if not bookname:
            return HttpResponse("Please pass the book name to api to list for the matching books")
        params={"name":bookname}

        ## we can implement redis catching for to recude load on api for repeated requests.

        matching_response=requests.get("https://www.anapioficeandfire.com/api/books",params=params)

        data1=[]
        if not matching_response.text:
            data=[]
        else:
            data=pd.io.json.json_normalize(json.loads(matching_response.text))[['name','isbn','authors','numberOfPages','publisher','country','released']]

        response={

            "status_code": 200,
            "status": "success",
            "data": data.to_dict()

        }

        return JsonResponse(response)
    else:
        return HttpResponse("Only get method supported on this URL. If you want make add books using POST call please use POST http://localhost:8080/api/v1/books")

