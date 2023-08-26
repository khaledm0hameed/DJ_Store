from django.shortcuts import render
from .models import Info
from django.conf import settings
from django.core.mail import send_mail


def send_massege(request):
    if request.method == 'POST' :
        subject = request.POST['subject']
        massage = request.POST['massage']
        email = request.POST['email']
        print(subject,massage,email)

    myinfo = Info.objects.first()
    return render(request,'contact/contact.html',{'myinfo':myinfo})