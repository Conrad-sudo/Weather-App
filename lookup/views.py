from django.shortcuts import render

# Create your views here.

#This is the views file

#Points a request to the webpage that we made


def home(request):
    import json
    import requests
    url="https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=13E04B77-23D5-4D90-A60E-CF11884B87AD"
    api_request=requests.get(url)

    try:
        api_response=json.loads(api_request.content)
    except Exception as e:
        api_response="Error..."





    return render(request,'home.html',{"api":api_response})


def about(request):
    return render(request,'about.html',{})