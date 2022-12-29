from django.shortcuts import render
from zeep import Client
from django.http import HttpResponse


# SunWaySMS Webservice Username and Password (https://sunwaysms.com/free/)

wsdl = 'https://sms.sunwaysms.com/SMSWS/SOAP.asmx?wsdl'

client = Client(wsdl=wsdl)

array_of_string_type = client.get_type("ns0:ArrayOfString")
array_of_long_type = client.get_type("ns0:ArrayOfLong")

def index(request):
    return render(request,'base.html')


def getcredit(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        a = client.service.GetCredit(username, password)
        return HttpResponse(f'<p>موجودی حساب شما در پنل سان وی {a} ریال </p> <a href="http://127.0.0.1:8000">برگشت</a>')
    
    return render(request, 'getcredit.html')


def sendsms(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        RecipientNumber = request.POST.get('RecipientNumber1')
        RecipientNumber2 = array_of_string_type([RecipientNumber])
        MessageBody = request.POST.get('MessageBody')
        SpecialNumber = request.POST.get('SpecialNumber')
        c = client.service.SendArray(username, password, RecipientNumber2, MessageBody, SpecialNumber)
        return HttpResponse(f'<p>عملیات انجام شد کد پیگیری {c}</p> <a href="http://127.0.0.1:8000">برگشت</a>')
    return render(request,'sendsms.html')