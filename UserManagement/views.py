from django.shortcuts import render
from .models import User

def register_user(request):
    users= User.object.all()
    if request.method == 'POST':
        print(request.POST)
        users.fullname = request.POST['fname']
        users.email = request.POST['email']
        users.username = request.POST['uname']
        users.password = request.POST['upass']
        users.mobileno = request.POST['mnum']
        users.address = request.POST['address']
        users.save()
        return render(request,'UserRegistration.html')
    else:
        return render(request, 'AdminRegistration.html')

