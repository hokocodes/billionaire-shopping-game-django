from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pyrebase

config = {
  "apiKey": "AIzaSyAh-CjZAi1CXzPerTz7YiFflNVh110oXzw",
  "authDomain": "billionaireshoppinggame-django.firebaseapp.com",
  "databaseURL": "None",
  "projectId": "billionaireshoppinggame-django",
  "storageBucket": "billionaireshoppinggame-django.appspot.com",
  "messagingSenderId": "696913707660",
  "appId": "1:696913707660:web:a7fd12801966262f4cb1a9",
  "measurementId": "G-2TS3BJQWRF"
}

# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def signIn(request):
    return render(request,"Login.html")

def home(request):
    return render(request,"index.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"index.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")
 
def signUp(request):
    return render(request,"Registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "Registration.html")
     return render(request,"Login.html")