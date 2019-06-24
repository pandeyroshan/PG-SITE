from django.shortcuts import render
from .models import AdminAddress
from django.contrib import messages
from hostel.models import MessageData
from hostel.models import RoomType
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')


def home(request):
    if request.method == 'POST':
        data = request.POST.dict()
        nameData = data.get("name")
        emailData = data.get("email")
        messageData = data.get("message")
        dataObject = MessageData(name=nameData,email=emailData,message=messageData)
        dataObject.save()
        subject = 'Numero Uno Home'
        message = 'Thanks for your Query, we will get back to you soon.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [emailData]
        send_mail( subject, message, email_from, recipient_list )
    dataSet = AdminAddress.objects.all()
    data = dataSet[0]
    context = {
        'name' : data.name,
        'address' : data.address,
        'phone' : data.phone,
        'email' : data.email
    }
    return render(request,'hostel/index.html',context)
