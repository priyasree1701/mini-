from django.shortcuts import render
from django.http import HttpResponse
from airtable import Airtable
import re
import hashlib
airtable = Airtable('appsa9Pz4MHCU6SAE','userdetails',api_key='keyCF870WzQlzT3of')

airtables= Airtable('appsa9Pz4MHCU6SAE','medicines',api_key='keyCF870WzQlzT3of')
# Cate your views here.
def hi(request):
    return render(request, 'demoapp/hi.html')

def home(request):
    return render(request, 'demoapp/home.html')

def signUp(request):
    return render(request, 'demoapp/signup.html')

def signin(request):
    return render(request, 'demoapp/signin.html')

def contact(request):
    return render(request, 'demoapp/contact.html')


def home(request):
    return render(request, 'demoapp/home.html')

def medicine(request):
    return render(request, 'demoapp/medilist.html')

def registrationSuccess(request):
    print(request)
    name = request.POST["name"]
    username = request.POST['uname']
    password=request.POST['pwd']
    emailid=request.POST['email']
    phoneno=request.POST['pno']
    address=request.POST['adres']
    passwordhash= hashlib.md5(password.encode())
    userdata = airtable.search("Username", username)
    if (userdata != []):
        return render(request, "demoapp/signup.html", {"error": "username alrady"})
    userdata = airtable.search("Email", emailid)
    if (userdata != []):
        return render(request, "demoapp/signup.html", {"error": "email already registered"})
    userdata = airtable.search("Phoneno", phoneno)
    print(userdata)
    if (userdata != []):
        return render(request, "demoapp/signup.html", {"error": "invalid phonenumber"})



    user_details = {
        "Username":username,
        "Password":passwordhash.hexdigest(),
        "Name":name,
        "Email":emailid,
        "Phoneno":phoneno,
        "Address":address,
    }
    airtable.insert(user_details)


    return render(request, 'demoapp/registrationSuccess.html')

def loginsucess(request):
    username = request.POST['uname']
    password = request.POST['pwd']
    passwordhash = hashlib.md5(password.encode())
    userdata=airtable.search("Username",username)
    if(userdata==[]):
        return render(request,"demoapp/signin.html",{"error":"invalid username"})
    if(passwordhash.hexdigest()!=userdata[0]["fields"]["Password"]):
        return render(request, "demoapp/signin.html", {"error": "invalid password"})
    return render(request,"demoapp/loginsucc.html")




def medilist(request):
    print(request)
    n = request.POST["mediname"]


    medicine_details = {
        "MedName":n,


}
    airtables.insert(medicine_details)
    return render(request, "demoapp/medilist.html")


