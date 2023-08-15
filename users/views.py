from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def registerUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirm_password")
        print(username,firstname,lastname,email,password,confirmpassword )

        if password == confirmpassword:
            users = User.objects.create_user(
                username = username,
                first_name = firstname,
                last_name = lastname,
                email = email,
                password = password
            )
            users.save()
        return redirect("home")
      


    return render(request, "index1.html")

@login_required
def loginUser(request):
 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect("home") 
        else:
            print("Users Validation Failed -401")
            return redirect("users:signin")
        
    return render(request, "login.html")
   

def logoutUser(request):
    logout(request)

    return redirect("home")

def forgetPassword(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmpassword = request.POST.get("confirm_password")

        try:
            user = User.objects.get(username=username)
            print(f"User found: {user}")
            
            if password == confirmpassword:
                user.set_password(password)
                user.save()
                print("Password reset successful")
                return redirect("users:signin")
            else:
                print("Passwords do not match")
                return render(request, "forget_password.html", {"error": "Passwords do not match"})
        except User.DoesNotExist:
            print(f"User with username {username} not found")
            return render(request, "forget_password.html", {"error": "Username not found"})

    return render(request, "forget_password.html")







