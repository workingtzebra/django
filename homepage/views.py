from django.shortcuts import render, redirect
from .models import Contact, CustomUser
from django.http import JsonResponse
from django.contrib.auth import authenticate, login#doin it to use django's default system

# Create your views here.
def loadhome(request):
   return render(request, 'homepage/home.html')#homepage is inside the templates


def loadcontact(request):
   return render(request, 'homepage/contact.html')


def contact_submit(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        #alreddy exits
        if Contact.objects.filter(email=email).exists():
            return JsonResponse({'error': 'User already present'})
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        return redirect('success')  # Redirect to a success def

    return render(request, 'homepage/contact.html')

def success(request):
    return render(request, 'homepage/success.html') 

def successRegister(request):
    return render(request, 'homepage/newUserSuccess.html') 

def register(request):
    return render(request, 'homepage/register.html') 

# def register_submit(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password=request.POST.get('password')
#         # message = request.POST.get('message')

#         #alreddy exits
#         if registerUser.objects.filter(email=email).exists():
#             return JsonResponse({'error': 'User already present'})
#         contact = registerUser(name=name, email=email, password=password)
#         contact.save()
#         return redirect('successRegister')  # Redirect to a success def

#     return render(request, 'homepage/contact.html')
def register_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Already exists
        if CustomUser.objects.filter(email=email).exists():
            error_message = 'User already exists with this email.'
            return render(request, 'homepage/register.html', {'error_message': error_message})
        
        # Create a new user using the CustomUser model
        user = CustomUser(name=name, email=email)
        user.set_password(password)  # Set the hashed password
        user.save()

        return redirect('successRegister')  # Redirect to a success def

    return render(request, 'homepage/contact.html')

def login_submit(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authentication
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecting to home for now
        else:
            # Invalid credentials
            return JsonResponse({'error': 'Invalid email or password'})

    # In case it's not a POST request
    return render(request, 'login.html')