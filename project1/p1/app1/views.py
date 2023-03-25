from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User


# Create your views here.
def first(request):
    if request.method=='POST':
        y=request.POST['fname']
        b=request.POST['sname']
        c=request.POST['class']
        d=request.POST['div']
        im=request.FILES['img']
        school(fnames=y,snames=b,classes=c,divi=d,imag=im).save()   
        return render(request,'studentform.html')
    return render(request,'studentform.html')

def tab(request):
    x=school.objects.all()
    y={'pin':x}
    return render(request,'table.html',y)
def viewbtn(request,v_id):
    vi=school.objects.get(id=v_id)
    return render(request,'viewbtn.html',{'btn':vi})
def updates(request,u_id):
    u=school.objects.get(id=u_id)
    if request.method=='POST':
        u.fnames=request.POST['fnam']
        u.snames=request.POST['snam']
        u.classes=request.POST['cla']
        u.divi=request.POST['di']
        u.save()
        return redirect(tab)
    return render(request,'update.html',{'updatebtn':u})
def dele(request,d_id):
    de=school.objects.get(id=d_id)
    de.delete()
    return redirect(tab)
def index(request):
    return render(request,'index.html')
def search(request):
    if request.method=='POST':
        se=request.POST['sear']
        sea=school.objects.filter(fnames=se)
        dict={'pin':sea}
        return render(request,'table.html',dict)
def register(request):
    if request.method=='POST':
        us=request.POST['user']
        first=request.POST['fname']
        second=request.POST['sname']
        email=request.POST['email']
        password1=request.POST['pass']
        password2=request.POST['cpass']
        if password1==password2:
            if User.objects.filter(username=us):
                print("USERNAME ALREADY EXISTS")
                return render(request,'register.html')
            elif User.objects.filter(email=email):
                print("email already exist")
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=us,first_name=first,last_name=second,email=email,password=password1)
                user.save()
                print("saved")
                return redirect(login)
        else:
            print("password doesnot match")
            return render(request,'register.html')
    else:
        return render(request,'register.html')    




