from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Payment,Profile
from .forms import ApplicatioForm
from datetime import datetime
# Create your views here.
@csrf_exempt
def index(request):
    print(request.POST)
    if request.method == 'POST':
        form = ApplicatioForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved"*10)
        else:
            print(form.errors)

    return render(request,'index.html')

@csrf_exempt
def status(request):
    print(request)
    if request.method == "POST":
        print("request recieved")
        print(request.POST)
        data = request.POST.get('phone')
        print(data)
        profile = Profile.objects.filter(phone = data)
        print(profile)
        return render(request,'status.html',{'profile':profile})
        
    return render(request,'status.html')

def adminsite(request):
    profiles = Profile.objects.all()

    return render(request,'admin.html',{'profiles':profiles})

def profileupdate(request,phone):
    profile = Profile.objects.filter(phone=phone)

    if request.method == "POST":
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        if not date:
            date = datetime.now()
        payment = Payment.objects.create(profile=profile,amount=amount,date=date)
        

    return render(request,'profileupdate.html')