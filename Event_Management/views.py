from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from .models import Booking, Contacts


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):    
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # create an instance of the model and save it to the database
        new_contact = Contacts(name=name,email=email,message=message)
        new_contact.save()
        return HttpResponse("Your Message has been submitted")
    else:
        return render(request,'contact.html')

def events(request):
    bookings = Booking.objects.all().order_by("-date")  # get all objects from Booking ordered by date in
    context={'bookings':bookings}   # pass the queryset to the template
    return render(request,'events.html')

def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        event_name = 'event_name' in request.POST
        date = 'date' in request.POST
        new_message=Booking(name=name,email=email,phone=phone,event_name=event_name,date=date)
        new_message.save()
        return redirect('events')
    return render(request,'booking.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('profile')
        else:
                return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
             my_user = User.objects.create_user(uname, email, pass1)
             my_user.save()
        return redirect('booking')
    return render(request, 'signup.html')

def wedding(request):
    return render(request,'wedding.html')

def eng(request):
    return render(request,'eng.html')

def rece(request):
    return render(request,'rece.html')

def par(request):
    return render(request,'par.html')

def bir(request):
    return render(request,'bir.html')

def get(request):
    return render(request,"get.html")

@login_required
def logoutt(request):
    logout(request)
    return redirect('/login/')

