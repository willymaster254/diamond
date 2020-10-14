from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import reverse
from django.contrib.auth.models import User, auth
from Home.models import Orders
from .forms import EmployeeForm

# Create your views here.
def contact(request):
    return render(request, 'contact.html')



def tutorsignup(request):
    return render(request, 'tutorsignup.html')

def orderlist(request):
    orders = Orders.objects.all()
    return render(request, 'orderlist.html', {'orders': orders})

def daniel(request):
    return render(request, 'Daniel.html')

def isaiah(request):
    return render(request, 'isaiah.html')

def zephy(request):
    return render(request, 'zephy.html')

def kate(request):
    return render(request, 'Kate.html')

def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def terms(request):
    return render(request, 'terms.html')


def home(request):
    return render(request, 'home.html')


def grading(request):
    return render(request, 'gradingsystem.html')


def services(request):
    return render(request, 'discipline.html')


def talk(request):
    return render(request, 'contact.html')


def rate(request):
    return render(request, 'Rate.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name, last_name=last_name)
                user.save();
                messages.success (request, f'Account Created Successfully!')
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching!')
            return redirect('register')
        return redirect('/') 

    else:
        return render(request, 'register.html')


def order(request):
    return render(request, 'order.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def list(request):
    from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_list.html", context)



def employee(request):
    if request.method == "GET":
        form= EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})
    else:
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')


def employee_delete(request):
    return



