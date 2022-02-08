from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Registration, Registered, Contact, Story
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
    
def editor(request):
    return render(request,  'tiny.html')
    # return HttpResponse("this is homepage")
    

def timeline(request):
    return render(request, 'timeline.html')


def give(request):
    return render(request, 'give.html')

def about(request):
    return render(request, 'about.html') 

def registered(request):
    registered_list= Registered.objects.all()
    return render(request, 'Registered Alumni.html', {'registered_list':registered_list})

def givingback(request):
    return render(request, 'giving back.html')

def gallery(request):
    return render(request, 'gallery.html')

def arrangement(request):
    return render(request, 'arrangement.html')

def meetings(request):
    return render(request, 'meetings.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passout = request.POST.get('passout')
        receipt = request.POST.get('receipt')
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        phone3 = request.POST.get('phone3')
        birthday = request.POST.get('birthday')
        profession = request.POST.get('profession')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        desc = request.POST.get('desc')
        registration = Registration(name=name, receipt=receipt, birthday=birthday, branch=branch, profession=profession, address1=address1, address2=address2, passout=passout, email=email, phone1=phone1, phone2=phone2, phone3=phone3,desc=desc, date= datetime.today())
        registration.save()
        messages.success(request, 'Your Registration Form Has Been Sent!')
        return render(request, 'registration.html')
    return render(request, 'registration.html')
 
def story(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passout = request.POST.get('passout')
        
        branch = request.POST.get('branch')
        email = request.POST.get('email')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        phone3 = request.POST.get('phone3')
        birthday = request.POST.get('birthday')
        profession = request.POST.get('profession')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        desc = request.POST.get('desc')
        story = Story(name=name, birthday=birthday, branch=branch, profession=profession, address1=address1, address2=address2, passout=passout, email=email, phone1=phone1, phone2=phone2, phone3=phone3,desc=desc, date= datetime.today())
        story.save()
        messages.success(request, 'Your Story Has Been Sent!')
        return render(request, 'story.html')
    return render(request, 'story.html')