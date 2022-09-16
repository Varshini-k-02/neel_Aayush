import random
import string
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from base.models import User,Complaint,Comment, ProgressBar
from django.contrib import messages
from .forms import SignUpForm, LoginForm, CompForm
from django.core import serializers

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def loginPage(request):
    page = 'login'
    form = LoginForm(request.POST or None)
    messages = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(username)
            # print(password)
            try:
                user = User.objects.get(username=username)
                employee1 = User.objects.get(username=username)
            except:
                return None
            print(user)
            authh = authenticate(username=username, password=password)
            
            if user is not None and user.is_user:
                login(request, user)
                return redirect('userdash')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('empdash')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admincomp')
            elif user is not None and (user.is_user == False & user.is_employee == False & user.is_admin == False):
                login(request, user)
                return redirect('userdash')
            else:
                messages= 'invalid credentials'
        else:
            messages = 'error validating form'
    return render(request,'base/reg_form.html', {'form': form, 'messages': messages,'page':page})

def registerPage(request):
    # messages = ''
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            user.save()
            print(user)
            # messages.info(request, 'User created')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    else:
        form = SignUpForm()
    return render(request,'base/reg_form.html', {'form': form, 'messages': messages})

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def complaint(request):
    form = CompForm()
    comp = Complaint.objects.all()
    tid=pwd()
    if request.method =='POST':
        Complaint.objects.create(
        ticketid=tid,
        complainant=request.user,
        type=request.POST.get("type"),
        subject = request.POST.get('subject'),
        desc = request.POST.get('desc'),
        docLink = request.POST.get('link'),
        )
    return render(request,'base/complaint.html')
def table(request):
    return render(request,'base/table.html')
    
def pwd():
    dummy_str = ''.join((random.choice(string.ascii_letters) for i in range(2)))
    dummy_str+=''.join((random.choice(string.digits) for i in range(3)))
    dummy_list=list(dummy_str)
    final_pwd=''.join(dummy_list)
    return final_pwd

#EMAIL AUTHENTICATION
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def empdashboard(request):
    comp=Complaint.objects.all()
    count=comp.count()
    cnt=0
    for i in comp:
        if i.status == '':
            cnt=cnt+1
    
    return render(request,'base/empdash.html',{'count':count,'cnt':cnt})
def empcategory(request):
    return render(request,'base/empcategory.html')
def empallcomp(request):
    # data = serializers.serialize("python",Complaint.objects.all())
    comp = Complaint.objects.all()

    # tid=comp.ticketid()
   
    return render(request,'base/empallcomp.html',{'comp':comp})

def assignment(request,pk):
    comp = Complaint.objects.get(ticketid=pk) #SEND ticketid for checking
    comp.handler = str(request.user)
    comp.status = "In-Progress"
    comp.save()
    return render(request,'base/extra.html')

def escalate(request,pk):
    comp=Complaint.objects.get(ticketid=pk)
    tid=comp.ticketid
    cmpt=comp.complainant
    ty=comp.type
    sub=comp.subject
    ds=comp.desc
    link=comp.docLink
    hdlr=comp.handler
    sts=comp.status
    
    return render(request,'base/escalate.html')
    
def comment(request,pk):
    compp = Complaint.objects.all()
    comp = Complaint.objects.get(ticketid=pk)
    # cc = comp.comment_set.all()

    if request.method == 'POST':
        Comment.objects.create(
                commenter=request.user,
                ticketid = comp,
                body = request.POST.get('body'),
        )

        return redirect('comment', pk=comp.ticketid)
    return render(request,'base/comment.html',{'comp':comp})

def progress(request,pk):
    compp=Complaint.objects.get(ticketid=pk)
    if request.method =='POST':
        ProgressBar.objects.create(
            commentee=request.user,
            tid = compp,
            bar=request.POST.get('barbody'),

        )
        return redirect('comment',pk=compp.ticketid)
    return render(request,'base/comment.html')


def userdashboard(request):
    comp=Complaint.objects.all()
    return render(request,'base/userdash.html',{'comp':comp}) 
def usercreatecomp(request):
    return render(request,'base/usercomp.html')

# *********************


def usercompstatus(request):
    bar=ProgressBar.objects.all()
    comp=Complaint.objects.all()
    
    return render(request, 'base/usercompstatus.html',{'comp':comp,'bar':bar})

# ****************************

def userprofile(request):
    return render(request,'base/userprofile.html')

# def status(request,pk):
#     comp=Complaint.objects.get(ticketid=pk)
#     return render(request,'base/status.html',{'comp':comp})

# def adminallcomp(request):
#     comp = AdminComp.objects.all()
#     return render(request,'base/adminallcomp.html',{'comp':comp})
# def fileUpload(request,pk):
#     comp = Complaint.objects.get(ticketid=pk)

#     return None

# def docSub(request,pk):
#     comp = Complaint.objects.get(ticketid=pk)
#     context={}
#     if comp.docs != None:
#         context={'file':comp.docs}
#     return render(request, 'base/complaint.html',context)
# def regComp(request)

def about(request):
    return render(request,'base/about.html')
def tandc(request):
    return render(request,'base/tandc.html')
# 
def support(request):
    return render(request,'base/support.html')
def privacy(request):
    return render(request,'base/privacy.html')

def emppending(request):
    comp=Complaint.objects.all()
   
    return render(request,'base/emppending.html',{'comp':comp})