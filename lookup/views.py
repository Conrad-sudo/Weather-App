from django.shortcuts import render

# Create your views here.

#This is the views file

#Points a request to the webpage that we made


def home(request):
    import json
    import requests

    resp=""
    color=""
    url="https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=13E04B77-23D5-4D90-A60E-CF11884B87AD"
    api_request=requests.get(url)

    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api="Error..."

    name=api[0]["Category"]["Name"]

    if name == "Good":

        resp="(0 - 50) Air quality is considered satisfactory, and air poses little to no risk "
        color="good"

    elif name == "Moderate":
        resp="(51-100) Air quality is acceptable.However, for some pollutants there can be slight health concerns"
        color="moderate"

    elif name == "Unhealthy for Sensitive Groups":
        resp="(101-150) The general public may not be affected. However, this AQI poses a risk to those with lung disease"
        color="usg"

    elif name == "Unhealthy":
        resp=" (151-200) Everyone may begin to experience health effects."
        color="uh"

    elif name == "Very Unhealthy":
        resp=" (201-300) Health alert. Everyone may experience more serious health effects."
        color="vuh"


    elif name == "Hazardous":
        resp="(301-500) Health warning of emergency conditions."
        color="hazardous"




    return render(request,'home.html',{"api":api , "description":resp,"colour_category":color})


def about(request):
    return render(request,'about.html',{})