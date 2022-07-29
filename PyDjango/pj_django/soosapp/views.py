from multiprocessing import context
from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Address, Gesipan

#def index(request):
#    return HttpResponse("<center><h3>안녕 장고^^</h3></center>")

def index(request):
    temlate = loader.get_template('index.html')
    #return HttpResponse(temlate.render())
    return HttpResponse(temlate.render({}, request)) # 반드시 request 넘겨줘야함!!

from django.db.models import Q
def list(request): # CRUD중 R에 해당하는 Read 를 담당하는 메서드
    temlate = loader.get_template('list.html')
    #addresses = Address.objects.all().values()
    #addresses = Address.objects.filter(name='홍길동').values() # WHERE 조건문
    #addresses = Address.objects.filter(name='홍길동',addr='서울시').values() # WHERE에 AND를 사용한 조건문
    #addresses = Address.objects.filter(name='홍길동').values() | Address.objects.filter(addr='서울시').values() # WHERE에 OR을 사용한 조건문
    #addresses =  Address.objects.filter(Q(name='홍길동') | Q(addr='서울시')).values() # WHERE에 OR을 사용한 조건문인데 Q라는 함수로 줄인것.
    #addresses =  Address.objects.filter(name__startswith='이')
    #addresses =  Address.objects.filter(name__startswith='이').values() #차이는 없다.
    #addresses = Address.objects.all().order_by('name').values() # ASC(오름차순) 은 생략이 가능
    #addresses =  Address.objects.all().order_by('-name').values()
    addresses =  Address.objects.all().order_by('-name', 'addr', '-id').values() #order by 를 여러개 사용
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))
 
def write(request): # CRUD중 C에 해당하는 Create 를 담당하는 메서드
	temlate = loader.get_template('write.html')
	return HttpResponse(temlate.render({},request))

from django.urls import reverse
from django.utils import timezone
def write_ok(request): # Create 이후 확인을 해주는 메서드
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id): # CRUD중 D에 해당하는 Delete 를 담당하는 메서드
	address = Address.objects.get(id=id)
	address.delete()
	return HttpResponseRedirect(reverse('list'))

def update(request, id): # CRUD중 U에 해당하는 Update 를 담당하는 메서드
    temlate = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address':address,
    }
    return HttpResponse(temlate.render(context, request))

def update_ok(request, id):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address.rdate = nowDatetime
    address.save()
    return HttpResponseRedirect(reverse('list'))

def glist(request):
    temlate = loader.get_template('glist.html')
    addresses =  Gesipan.objects.all().values()
    context = {
        'addresses': addresses, 
    }
    return HttpResponse(temlate.render(context, request))

def gwrite(request): 
	temlate = loader.get_template('gwrite.html')
	return HttpResponse(temlate.render({},request))

def gwrite_ok(request): 
    x = request.POST['write']
    y = request.POST['email']
    s = request.POST['subject']
    c = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Gesipan(write=x, email=y, subject=s, content=c, tdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('glist'))

def content(request, id):
    temlate = loader.get_template('content.html')
    address = Gesipan.objects.get(id=id)
    context = {
        'address':address,
    }
    return HttpResponse(temlate.render(context, request))

def gdelete(request, id): # CRUD중 D에 해당하는 Delete 를 담당하는 메서드
	address = Gesipan.objects.get(id=id)
	address.delete()
	return HttpResponseRedirect(reverse('glist'))

def gupdate(request, id): # CRUD중 U에 해당하는 Update 를 담당하는 메서드
    temlate = loader.get_template('gupdate.html')
    address = Gesipan.objects.get(id=id)
    context = {
        'address':address,
    }
    return HttpResponse(temlate.render(context, request))

def gupdate_ok(request, id):
    address = Gesipan.objects.get(id=id)
    y = request.POST['email']
    s = request.POST['subject']
    c = request.POST['content']
    address.email = y
    address.subject = s
    address.content = c
    address.save()
    return HttpResponseRedirect(reverse('glist'))

from django.shortcuts import redirect, render #방법2
def login(request):
    template = loader.get_template('login.html') #방법1
    return HttpResponse(template.render({}, request)) #방법1
    #return render(request,'login.html') #방법2 

from .models import Member 
def login_ok(request):
    #email = request.POST['email']
    #pwd = request.POST['pwd']
    email = request.POST.get('email', None)
    pwd = request.POST.get('pwd', None)
    print("email", email, "pwd", pwd)
    
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        member = None
    print("member", member)
    
    result = 0
    if member != None:
        print("해당 email회원 존재함")
        if member.pwd == pwd:
            print("비밀번호까지 일치")
            result = 2
            
            print("member.email:", member.email) # 방법1
            request.session['login_ok_user'] = member.email # 방법1
            
            #session_id = request.session.session_key # 방법2
            #print("sseesion.id:", session_id) # 방법2
            #request.session['login_ok_user'] = session_id # 방법2
        else:
            print("비밀번호 틀림")
            result = 1
    else:
        print("해당 email회원 존재하지 않음")
        result = 0
        
    temlate = loader.get_template("login_ok.html")
    context = {
        'result': result
    }
    return HttpResponse(temlate.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        request.session.clear() # 서버측의 해당 user의 session방을 초기화
        #request.session.flush() # 서버측의 해당 user의 session방을 삭제
    return redirect("../") # redirect 다시 요청? 뜻을 찾아보자