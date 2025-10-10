from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserRegistration, AdminUser
from django.contrib import messages

import random
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegistration
from django.conf import settings

import traceback

from django.db import IntegrityError
from django.contrib import messages


# -------- User Signup --------


from django.shortcuts import render
from EduTrack.models import UserRegistration

def signup(request):
    import traceback

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
   return render(request, 'addvisiter.html')
def newpassword(request):
    uid = request.session.get('reset_user_id')
    if not uid:
        return redirect('send_otp')  # redirect to OTP send view

    try:
        user = UserRegistration.objects.get(id=uid)
    except UserRegistration.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('send_otp')

    if request.method == 'POST':
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 and p1 == p2:
            user.set_password(p1)
            user.save()
            messages.success(request, "Password reset successful. You can now login.")
            return redirect('fuk')  # user login page
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'newpassword.html')
    





# -------- Verify OTP --------
def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = str(request.session.get('otp'))

        if entered_otp == session_otp:
            messages.success(request, "OTP verified successfully.")
            return redirect('newpassword')
        else:
            messages.error(request, "Invalid OTP. Try again.")

    return render(request, 'verify_otp.html')


# -------- Reset Password (Your newpassword view) --------

