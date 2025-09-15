from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def home(request):
    std  = Student.objects.all()
    return render(request, 'std/home.html', {'std':std})

def std_add(request):
    if request.method=='POST':
        print("added")
        stdroll = request.POST.get('roll')
        stdname = request.POST.get('name')
        stdemail = request.POST.get('email')
        stdaddress = request.POST.get('address')
        stdphone = request.POST.get('phone')

        s=Student()
        s.roll=stdroll
        s.name=stdname
        s.email=stdemail
        s.address=stdaddress
        s.phone=stdphone

        s.save()
        return redirect("/std/home")

    return render(request, "std/add_std.html", {})


def delete_std(request, roll):
    s=Student.objects.get(pk=roll)
    s.delete()

    return redirect('/std/home')

def update_std(request, roll):
    std = Student.objects.get(pk=roll)
    return render(request, "std/update_std.html", {'std':std})


def do_update_std(request, roll):
   
    stdroll = request.POST.get('roll')
    stdname = request.POST.get('name')
    stdemail = request.POST.get('email')
    stdaddress = request.POST.get('address')
    stdphone = request.POST.get('phone')

    s=Student.objects.get(pk=roll)

    s.roll=stdroll
    s.name=stdname
    s.email=stdemail
    s.address=stdaddress
    s.phone=stdphone

    s.save()
   
    return redirect('/std/home')