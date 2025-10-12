

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserRegistration, AdminUser,Visiterdata
from django.contrib import messages

import random

from django.contrib import messages
from .models import UserRegistration
from django.conf import settings

import traceback




# -------- User Signup --------


from django.shortcuts import render
from EduTrack.models import UserRegistration
import traceback
def signup(request):
    

    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            # Password confirm check
            if password != confirm_password:
                return render(request, 'signup.html', {'error': 'Passwords do not match'})

            # Duplicate username check
            if UserRegistration.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Username already taken'})

            # User create
            user = UserRegistration(
                name=name,
                mobile=mobile,
                address=address,
                username=username
            )
            user.set_password(password)  # Hash password
            user.save()

            return render(request, 'signup.html', {'success': 'User registered successfully!'})

        # GET request
        return render(request, 'signup.html')

    except Exception as e:
        # Print full traceback in console for debugging
        print(traceback.format_exc())
        return render(request, 'signup.html', {'error': f'Unexpected error: {str(e)}'})

# -------- User Login --------
# -------- User Login --------
def fuk_view(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            user = UserRegistration.objects.get(username=username)
        except UserRegistration.DoesNotExist:
            return render(request, 'fuk.html', {'error': 'Invalid username or password'})

        if user.check_password(password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['is_admin'] = False
            return redirect('home')
        else:
            return render(request, 'fuk.html', {'error': 'Invalid username or password'})

    return render(request, 'fuk.html')


# -------- Admin Login --------
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        try:
            admin = AdminUser.objects.get(username=username)
        except AdminUser.DoesNotExist:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

        if admin.check_password(password):
            request.session['user_id'] = admin.id
            request.session['username'] = admin.username
            request.session['is_admin'] = True
            return redirect('home')
        else:
            return render(request, 'admin.html', {'error': 'Invalid username or password'})

    return render(request, 'admin.html')

# -------- Home Page --------
def index(request):
    context = {
        'username': request.session.get('username'),
        'is_admin': request.session.get('is_admin', False)
    }
    return render(request, 'index.html', context)

# -------- Logout --------
def logout_view(request):
    request.session.flush()
    return redirect('home')

# -------- Student Data (Admin) --------
def studentdata(request):
    students = UserRegistration.objects.all()
    return render(request, 'student_data.html', {'students': students})

# -------- Delete Student --------
def delete_student(request, id):
    student = get_object_or_404(UserRegistration, id=id)
    student.delete()
    return redirect('studentdata')

    
def about(request):
   return render(request, 'about.html')


def visiter(request):

   try:
    if request.method=="POST":
       name=request.POST.get("name")
       email=request.POST.get("email")
       phone=request.POST.get("phone")
       purpose=request.POST.get("purpose")
       if Visiterdata.objects.filter(email=email).exists():
                return render(request, 'visiter.html', {'error': 'Email already exists'})

       if Visiterdata.objects.filter(name=name).exists():
                return render(request, 'visiter.html', {'error': 'visiter already taken'})

       visiter=Visiterdata(
       name=name,
       email=email,
       phone=phone,
       purpose=purpose
       )
       visiter.save()
     
       print("Saved visiter:", visiter.id)
       return render(request,"visiter.html",{'success':'visiter successfully added ✅'})
    return render(request,"visiter.html")
   except Exception as e:
        print(traceback.format_exc())
        return render(request, 'visiter.html', {
    'error': 'Visiter already taken',
    'name': name,
    'email': email,
    'phone': phone,
    'purpose': purpose
})

