from django.shortcuts import render,redirect
from .models import Guser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .forms import LoginForm
def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('/')
def home(request):
    user_id = request.session.get('user')
    if user_id: 
        guser = Guser.objects.get(pk=user_id)
        return HttpResponse(guser.username) 
    return HttpResponse('welcome Home')
def login(request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})
    # if request.method=="GET":
    #     return render(request,'login.html')
    # elif request.method == "POST":
    #     username= request.POST.get('username',None)
    #     password = request.POST.get('password',None)
    #     res_data={}
    #     if not (username and password):
    #         res_data['error']='모든값을 입력하세요'
    #     else:
    #         guser=Guser.objects.get(username=username)
    #         if check_password(password,guser.password):
    #             request.session['user']=guser.id
    #             return redirect('/')
    #         else:
    #             res_data['error']='비밀번호가 일치하지 않습니다.'
    #     return render(request,'login.html',res_data)
def register(request):
    if request.method=="GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username= request.POST.get('username',None)
        useremail= request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password =request.POST.get('re_password',None)
        
        res_data={}
        if not (username and password and re_password and useremail):
            res_data['error']='모든값을 입력하세요'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다'

        else:
            guser = Guser(
                username = username,
                useremail= useremail,
                password = make_password(password)
            )
            guser.save()
        return render(request,'register.html',res_data)

