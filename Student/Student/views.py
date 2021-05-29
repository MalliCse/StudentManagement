from django.shortcuts import render
from django.contrib import messages
from Student.models import Insert,Register
from django.core.exceptions import ObjectDoesNotExist

def Insertrecord(request):
    if request.method == "POST":
       empname = request.POST.get('empname')
       email = request.POST.get('email')
       password = request.POST.get('password')
       #ins=Insert(empname=empname,email=email,password=password)
       temp=Register.objects.get(stdname=empname)
       print(temp.email)
       if(temp.email == email and temp.stdname == empname and password == temp.password and 'admin' in email):
          print("Hii")
          return render(request,'SuccessAdminLogin.html')
       elif(temp.email == email and temp.stdname == empname and password == temp.password and 'student' in email):
          print("hello")
          return render(request,'SuccessStudentLogin.html')
       else:
          return render(request,'FailureAdminLogin.html')


    return render(request,'index.html')

def Registerrecord(request):
    if request.method == "POST":
       stdname = request.POST.get('stdname')
       email = request.POST.get('email')
       password = request.POST.get('password')
       stdid = request.POST.get('stdid')
       gender= request.POST.get('gender')
       contact= request.POST.get('contact')
       total_fee = request.POST.get('total_fee')
       paid_fee = request.POST.get('paid_fee')
       dob=request.POST.get('dob')
       address=request.POST.get('address')
       ins=Register(stdname=stdname,email=email,password=password,stdid=stdid,gender=gender,contact=contact,total_fee=total_fee,paid_fee=paid_fee,dob=dob,address=address)
       ins.save()
       print(stdname,email,password,contact,paid_fee)
       print("Data has been returned")
       
       return render(request,'SuccessRegister.html')

    return render(request,'AdminRegister.html')

def Home(request):
   return render(request,'Home.html')

def Contact(request):
   return render(request,'Contact.html')

def About(request):
   return render(request,'About.html')

def LoginView(request):
   return render(request,'LoginView.html')

def LoginView1(request):
   if request.method == "POST":
       stdid = request.POST.get('stdid')
       try:
         temp=Register.objects.get(stdid=stdid)
         return render(request,'LoginViewSuccess.html',{'temp' : temp})
       except ObjectDoesNotExist:
         print("Either the blog or entry doesn't exist.")
         return render(request,'LoginViewFailure.html')
         
   
   
   return render(request,'Home.html')

def StudentView(request):
   if request.method == "POST":
       stdid = request.POST.get('stdid')
       try:
         temp=Register.objects.get(stdid=stdid)
         return render(request,'StudentLoginViewSuccess.html',{'temp' : temp})
       except ObjectDoesNotExist:
         print("Either the blog or entry doesn't exist.")
         return render(request,'LoginViewFailure.html')
         
   
   
   return render(request,'StudentLoginView.html')

def Edit(request):
    if request.method == "POST":
       stdid = request.POST.get('stdid')
       try:
         temp=Register.objects.get(stdid=stdid)
         return render(request,'ViewEditSuccess.html',{'temp' : temp})
       except ObjectDoesNotExist:
         print("Either the blog or entry doesn't exist.")
         return render(request,'ViewEditFailure.html')

def Logout(request):
   return render(request,'Logout.html')

def Delete(request):
   if request.method == "POST":
      stdid = request.POST.get('stdid')
      try:
         temp=Register.objects.get(stdid=stdid)
         temp.delete()
         return render(request,'DeleteViewSuccess.html',{'stdid' : stdid})
      except ObjectDoesNotExist:
         print("Either the blog or entry doesn't exist.")
         return render(request,'DeleteViewFailure.html')
   return render(request,'Delete.html')


def ViewEditSave(request):
    if request.method == "POST":
       stdid = request.POST.get('stdid')
       temp=Register.objects.get(stdid=stdid)

       temp.stdname = request.POST.get('stdname')
       temp.email = request.POST.get('email')
       temp.gender= request.POST.get('gender')
       temp.contact= request.POST.get('contact')
       temp.total_fee = request.POST.get('total_fee')
       temp.paid_fee = request.POST.get('paid_fee')
       temp.dob=request.POST.get('dob')
       temp.address=request.POST.get('address')
       #ins=Register(stdname=stdname,email=email,password=password,stdid=stdid,gender=gender,contact=contact,total_fee=total_fee,paid_fee=paid_fee,dob=dob,address=address)
       #ins.save()
       temp.save()
       #print(stdname,email,password,contact,paid_fee)
       print("Data has been returned")
       
       return render(request,'SuccessRegister.html')



   