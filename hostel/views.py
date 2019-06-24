from django.shortcuts import render
from .models import AdminAddress
from django.contrib import messages
from hostel.models import MessageData
# Create your views here.

def home(request):
    if request.method == 'POST':
        data = request.POST.dict()
        nameData = data.get("name")
        emailData = data.get("email")
        messageData = data.get("message")
        dataObject = MessageData(name=nameData,email=emailData,message=messageData)
        dataObject.save()
    dataSet = AdminAddress.objects.all()
    data = dataSet[0]
    context = {
        'name' : data.name,
        'address' : data.address,
        'phone' : data.phone,
        'email' : data.email
    }
    return render(request,'hostel/index.html',context)