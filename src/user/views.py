from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout




def register(request):
    if request.method =='POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'تهانينا {username} لقد تمت عملية التسجيل بنجاح')
            return redirect('home')

    else:
         form = UserCreationForm()    
    context = {
        'title': 'التسجيل',
        'form' : form
    }
    return render (request, 'user/register.html',context)


def login_user(request):
    if request.method == 'POST':
      form     = LoginForm()
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username = username, password = password)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.warning(request, 'هناك خطأ في كلمة المرور او اسم المستخدم')  
    else: 
      form = LoginForm() 
    context ={
        'title' : 'تسجيل دخول',
        'form'  : form
    }
    return render (request, 'user/login.html',context)


def logout_user(request):
    logout(request)   
    context={
        'title' : 'تسجيل الخروج'
    }
    return render(request, 'user/logout.html',context)