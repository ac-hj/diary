from django.shortcuts import render, redirect
from core.models import Diary
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# home page
def splash(request):
    # if logged in, show the user's notes
    if request.user.is_authenticated:
        author = request.user
        entries = Diary.objects.filter(author=author)
        # if the user creates new notes
        if request.method == "POST":
            print(request.POST["title"], request.POST["body"])
            title = request.POST["title"]
            body = request.POST["body"]
            Diary.objects.create(title=title, body=body, author=request.user)
        #  show all of the user's notes (including the new one)
        return render(request, "splash.html", {"entries": entries})
    # else, redirect to the login page
    else:
        return redirect("/login")
    
# login page
def login_view(request):
    # if the users enters in username and password
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    # if already  logged in
    elif request.user.is_authenticated:
        
        return redirect("/")
    # else, return the login pages (GET method)
    return render(request, 'accounts.html', {})

# logs out the user and redirects to the login page
def logout_2(request):
    logout(request)
    return redirect("/login")

# sign up route
def signup_view(request):
    # if user submits sign up info
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'],
                        email=request.POST['email'],
                        password=request.POST['password'])
        login(request, user)
        # redirect to the homepage after signing  up
        return redirect('/')
    # else, return registration page
    return render(request, 'registration.html', {})

