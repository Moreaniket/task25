from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home (request):
    return render(request,"index.html")
def save(request):
    if request.method=="POST":
        fn=request.POST["first_name"]
        ln=request.POST["last_name"]
        un=request.POST["username"]
        ps=request.POST["password"]

        data=User.objects.create_user(first_name=fn,last_name=ln,username=un,password=ps)
        data.save()
        return HttpResponse("Register Successfully")
    else:
        return HttpResponse("Fails..")



def signin(request):
    return render(request,"signin.html")

def check(request):
    if request.method=="POST":
        un=request.POST["username"]
        ps=request.POST["password"]

        data=authenticate(username=un,password=ps)
        if data:
            login(request,data)
            return redirect("/admin")
        else:
            return HttpResponse("Login Fails..")


def reset(request):
    return render(request,"reset.html")

def resetps(request):
    if request.method=="POST":
        un = request.POST["username"]
        ops = request.POST["old_password"]
        nps = request.POST["new_password"]

        data=authenticate(username=un,password=ops)
        if data:
            data.set_password(nps)
            data.save()
            return HttpResponse("Password Reset Successfully")
        else:
            return HttpResponse("fails to reset password")




from .models import shubham
from rest_framework.renderers import JSONRenderer
from.serializers import shubham_serializer
def one(request,id):
    data=shubham.objects.get(id=id)
    serializer=shubham_serializer(data)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")



def list(request):
    data=shubham.objects.all()
    serializer=shubham_serializer(data,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
@csrf_exempt
def add(request):
    if request.method=="POST":
        data=json.loads(request.body)
        shubham.objects.create(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
        return JsonResponse({"messages":"Added Successfully"})
    else:
        return JsonResponse({'Error':'Invalid Method'})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



@csrf_exempt
def update(request):
    if request.method=="PUT":
        data=json.loads(request.body)
        shubham.objects.filter(id=data["id"]).update(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
        return JsonResponse({"messages": "Update Successfully"})
    else:
        return JsonResponse({'Error': 'Invalid Method'})



@csrf_exempt
def delete(request):
    if request.method=="DELETE":
        data=json.loads(request.body)
        shubham.objects.filter(id=data["id"]).delete()
        return JsonResponse({'message':'Delete successfully'})
    else:
        return JsonResponse({'Error':'Invalid Method'})



@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        # Check if user exists with the provided email and password
        if shubham.objects.filter(email=email, password=password).exists():
            return JsonResponse({'msg': 'Login Successfully'})
        else:
            return JsonResponse({'Error': 'Invalid email or password'})

    return JsonResponse({'Error': 'Invalid request method'})


import requests
from django.shortcuts import render

def calculate(request):
    if request.method == "POST":
        # Get input values from the form
        source = request.POST.get('source')
        destination = request.POST.get('destination')

        if not source or not destination:
            return render(request, "index1.html", {
                "error": "Please enter both source and destination locations."
            })

        # API key and endpoint
        api_key = "AIzaSyCIviLdJVYIjvH7R9eq5OUN0Z4G5thHDIw"
        url = "https://maps.googleapis.com/maps/api/distancematrix/json"

        # Make the API request
        params = {
            "origins": source,
            "destinations": destination,
            "key": api_key
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Debugging: Print API response to check the format
        print(data)

        # Check for a valid response
        if data.get("status") == "OK" and data.get("rows"):
            elements = data['rows'][0]['elements']
            if elements and elements[0].get("status") == "OK" and "distance" in elements[0]:
                # Extract the distance in km
                distance = elements[0]['distance']['text']
                return render(request, "result.html", {
                    "source": source,
                    "destination": destination,
                    "distance": distance
                })

        # Render an error message if the response is invalid
        return render(request, "index1.html", {
            "error": "Unable to calculate distance. Please check the input locations and try again."
        })

    return render(request, "index1.html")




