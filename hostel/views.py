from django.shortcuts import render
from .models import AdminAddress
from django.contrib import messages
from hostel.models import MessageData
from hostel.models import RoomType
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    if request.method == 'POST':
        data = request.POST.dict()
        nameData = data.get("name")
        emailData = data.get("email")
        messageData = data.get("message")
        dataObject = MessageData(name=nameData,email=emailData,message=messageData)
        dataObject.save()
        subject = 'NUMERO UNO HOME'
        message = 'Dear '+nameData+'! We have recieved your Query, Our Assistant will get back to you soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emailData]
        send_mail( subject, message, email_from, recipient_list )
    dataSet = AdminAddress.objects.all()
    data = dataSet[0]
    RoomDataSet = RoomType.objects.all()
    doubleData = RoomDataSet[0]
    tripleData = RoomDataSet[1]
    fourData = RoomDataSet[2]
    context = {
        'name' : data.name,
        'address' : data.address,
        'phone' : data.phone,
        'email' : data.email,
        'doubleType': doubleData.roomType, 
        'doubleStatus': doubleData.status,
        'doubleRent': doubleData.rentMoney,
        'doubleNote': doubleData.shortNote,
        'tripleType': tripleData.roomType, 
        'tripleStatus': tripleData.status,
        'tripleRent': tripleData.rentMoney,
        'tripleNote': tripleData.shortNote,
        'fourType': fourData.roomType, 
        'fourStatus': fourData.status,
        'fourRent': fourData.rentMoney,
        'fourNote': fourData.shortNote
    }
    return render(request,'hostel/index.html',context)
