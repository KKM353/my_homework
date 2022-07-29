[ 'Part1' ] CRUD

1. ȯ�����
	(1) ���� Ȯ��
		1) $ python --version
		20 $ pip --version

	(2) ���� ȯ��(�ش� �������� ����Ǵ� ����ȯ�漳�� ����)
		

		[���̽� ��ü���� �����ϴ� ���]
		1) ����
			$ py -m venv env_django
			�Ǵ� 
			$ python -m venv env_django

			#����) �Ƴ��ܴٿ��� ����
			$conda create -n env_django python=3.9.6

		2) Ȱ��ȭ
			$ env_django\Scripts\activate.bat

			#����1) $ env_django\Scripts\deactivate.bat #��Ȱ��ȭ 
			#����2) �Ƴ��ܴٿ��� Ȱ��ȭ
			$conda activate env_django
	
	(3) ��� ����
		1) �ν���
			(env_django) C:\SOO\PyDjango> py -m pip install Django
			�Ǵ� 
			(env_django) C:\SOO\PyDjango> python -m pip install Django


			#����) �ʿ��ϸ� pip ���׷��̵� 
			(env_django) C:\SOO\PyDjango> py -m pip install --upgrade pip
		
		2) ����Ȯ��
			(env_django) C:\SOO\PyDjango> django-admin --version 

	(4) ������Ʈ ( 'pj_django' ) 
		1) ���� 
			(env_django) C:\SOO\PyDjango> django-admin startproject pj_django

		2) ����
			(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		3) ���������� Ȯ�� ( python cmd���� ������ ��ũ�� Ŭ���ϸ�ȴ�.)
			http://127.0.0.1:8000/

	(5) �� ( 'soosapp' )
		1) �������� 
			���� �������̶�� ������Ŵ ( Ctrl + C )

		2) ����
			(env_django) C:\SOO\PyDjango\pj_django> py manage.py startapp soosapp

2. ���� ( Views )
	(1) soosapp/views.py
	from django.http import HttpResponse
	from django.shortcuts import render

	def index(request):
		return HttpResponse("�ȳ� ���^^")
	
	(2) soosapp/urls.py ���� �� ���� 
		from django.urls import path
		from . import views

		urlpatterns = [
			path('', views.index, name='index'),
		]
		
	(3) pj_django/pj_django/urls.py ���� 
		from django.contrib import admin
		from django.urls import path
		from django.urls import include, path

		urlpatterns = [
			path('admin/', admin.site.urls),
			path('soosapp/', include('soosapp.urls')),
		]

	(4) �������� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/

3. ���ø���( Templates	 ) 
	(1) soosapp/templates/index.html ���� ���� (����+����) 
		<!DOCTYPE html>
		<center>
			<h1>Soo's index.html</h1>
		</center>

	(2) soosapp/views.py ���� 
		...
		from django.template import loader

		def index(request):
			temlate = loader.get_template('index.html')
			#return HttpResponse(temlate.render()) # ���߿� session�������� �������� ����
			return HttpResponse(temlate.render({}, request)) #�ݵ��!! request�� �Ѱ���� ��

	(3) pj_django/pj_django/settings.py ���� 
		INSTALLED_APPS = [
			...
			'soosapp.apps.SoosappConfig' #�̺κ� �߰�
		]
		
	(4) ���� (���̱׷�Ʈ)  
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py migrate
			
	(5) �������� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/ 	

4. ����( Models	) 
	(1) soosapp/models.py
		from django.db import models

		class Address(models.Model):
			name = models.CharField(max_length=200)
			addr = models.TextField()
			rdate = models.DateTimeField()

	(2) soosapp/migrations ��ɾ�� ���� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py makemigrations soosapp

		#���) migrations/0001_initial.py ����Ȯ�� ( Create model Address �� ) 

	(3) ���� (���̱׷�Ʈ) 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py migrate

		#���) Applying soosapp.0001_initial.py ���� ( SQLite DBMS�� ���� �� ) 

	(4) ������ ����� MySQL�� SQL�� �Ʒ��� ���� 
		create table Address (
			id int primary key autoincrement,
			name varchar(200), 
			addr text,
			rdate datetime
		);
		
5. DB���̺� ������ ���� 
	(1) Python shell â ���� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py shell

		#����) >>> quit()

	(2) Record �߰�
	    0) timezone ���� ( pj_django/pj_django/settings.py �� ���� )
			#TIME_ZONE = 'UTC'
			TIME_ZONE = 'Asia/Seoul'

			#USE_TZ = True
			USE_TZ = False

				
		1) 1��
			<1> ���1
				>>> from soosapp.models import Address
				>>> Address.objects.all()

				>>> from django.utils import timezone
				>>> print(timezone.now())
				>>> nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
				>>> print(nowDatetime)
				>>> address = Address(name='ȫ�浿', addr='�����', rdate=nowDatetime)
				>>> address.save()

				>>> Address.objects.all().values()

			<2> ���2
				>>> import datetime
				>>> now = datetime.datetime.now()
				>>> print(now)
				>>> nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
				>>> print(nowDatetime)
				>>> address = Address(name='������', addr='��õ��', rdate=nowDatetime)
				>>> address.save()

				>>> Address.objects.all().values()

		2) N�� 
			>>> address1 = Address(name='�̼���', addr='�λ��', rdate=nowDatetime)
			>>> address2 = Address(name='������', addr='���ֽ�', rdate=nowDatetime)
			>>> address3 = Address(name='��������', addr='������', rdate=nowDatetime)
			>>> address_list = [address1, address2, address3]
			>>> for x in address_list:
					x.save()
		    
			>>> Address.objects.all().values()

	(3) Record ���� 
		1) 1�� 
			>>> address = Address.objects.get(id=2)
			>>> address.delete()

		2) N��
			>>> addresses = Address.objects.all()
			>>> addresses.delete()

		3) Ȯ�� 
			>>> Address.objects.all().values()


6. 'R'ead 			
	(1) soosapp/views.py �� �߰�
		...
		from .models import Address

		def list(request):
			temlate = loader.get_template('list.html')
			addresses =  Address.objects.all().values()
			context = {
				'addresses': addresses, 
			}
			return HttpResponse(temlate.render(context, request))
		
	(2) soosapp/templates/list.html ���� �� ����
		<a href='../'>�ε���</a><br/>
	    ... 
		{% for address in addresses %}
		<tr>
		<td align='center'>{{address.id}}</td>
		<td>{{address.name}}</td>
		<td>{{address.addr}}</td>
		<td>{{address.rdate}}</td>
		<td align='center'><a href="">����</a></td>
		</tr>
		{% endfor %}
		...

	(3) soosapp/urls.py �� �߰�
		path('list/', views.list, name='list'), #�߰�

	(4) �������� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/list  

	(5) soosapp/templates/index.html �� ��ũ �߰� 
		<a href="list">ȸ��</a><br/>


7. 'C'reate ####### ���� �԰� ######
	(1) soosapp/templates/list.html ���� ��ũ ����
	    ...
		<a href='../write'>�Է�</a>  
		...

	(2) soosapp/templates/write.html ���� 
		...
		<form name="f" action="write_ok" method="post">
           {% csrf_token %}
		...
'''
	(3) soosapp/templates/js/trim.js ����  #���� ���� # �ٽ� �˾ƺ��� 4:15~
		function trim(str){
			while(str && str.indexOf(" ") == 0)
				str = str.substring(1); 
			while(str && str.lastIndexOf(" ") == str.length-1)
				str = str.substring(0, str.length-1); 
			return str;
		}
'''
	(3) static �������� �� ���� ( for 'trim.js' )
		<1> pj_django/pj_django/settings.py Ȯ��
			# Static files (CSS, JavaScript, Images)
			STATIC_URL = 'static/'

		<2> soosapp/static ���� ���� / �� ���� ������ ���� 
		    1> static/css
			2> static/img
			3> static/js/trim.js 

				function trim(str){
					while(str && str.indexOf(" ") == 0)
						str = str.substring(1); 
					while(str && str.lastIndexOf(" ") == str.length-1)
						str = str.substring(0, str.length-1); 
					return str;
				}
				
		<3> soosapp/templates/write.html
			...
			{% load static %}
			<script src="{% static '/js/trim.js' %}"></script>
			...

	(4) soosapp/views.py �� �߰� 
		def write(request):
			temlate = loader.get_template('write.html')
			return HttpResponse(temlate.render())

	(5) soosapp/urls.py �� �߰�
		path('write/', views.write, name='write'), #�߰�

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/

	(6) soosapp/urls.py �� �߰�2
		path('write/write_ok/', views.write_ok, name='write_ok'), #�߰�

	(7) soosapp/views.py �� �߰�2
		from django.urls import reverse 
		from django.utils import timezone
		def write_ok(request):
			x = request.POST['name']
			y = request.POST['addr']
			nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
			address = Address(name=x, addr=y, rdate=nowDatetime)
			address.save()
			return HttpResponseRedirect(reverse('list'))

	(8) �������� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/write
		

8. 'D'elete
	(1) soosapp/templates/list.html ����
		...
		<td align='center'><a href="../delete/{{address.id}}">����</a></td> 
		... 

		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/list ���� '����'�� ���콺����

	(2) soosapp/urls.py �� �߰�
		path('delete/<int:id>', views.delete, name='delete'), #�߰�

	(3) soosapp/views.py �� �߰� 
		def delete(request, id):
			address = Address.objects.get(id=id)
			address.delete()
			return HttpResponseRedirect(reverse('list'))


		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/list

9. 'U'pdate # �̼�
	(1) soosapp/templates/list.html ����
		...
		<td align='center'><a href="../update/{{address.id}}">{{address.id}}</a></td>
		...

	(2) soosapp/urls.py �� �߰�1
		path('update/<int:id>', views.update, name='update'), #�߰�

	(3) soosapp/templates/update.html ���� �� ����
		...
		{% load static %}
		<script src="{% static '/js/trim.js' %}"></script>
		...
		<form name="f" action="update_ok/{{address.id}}" method="post">
           {% csrf_token %}
		...
		<td><input name="name" value="{{address.name}}" align="center" size="20" align="center" onkeydown="enterCheck(this)"></td>
		...
		<td><input name="addr" value="{{address.addr}}" size="20" align="center" onkeydown="enterCheck(this)"></td>
		...

	(4) soosapp/views.py �� �߰�1 
		def update(request, id):
			temlate = loader.get_template('update.html')
			address = Address.objects.get(id=id)
			context = {
				'address': address, 
			}
			return HttpResponse(temlate.render(context, request))


		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/list

	
	(5) soosapp/urls.py �� �߰�2
		path('update/update_ok/<int:id>', views.update_ok, name='update_ok'), #�߰�

	(6) soosapp/views.py �� �߰�2
		def update_ok(request, id):
			x = request.POST['name']
			y = request.POST['addr']
			address = Address.objects.get(id=id)
			address.name = x
			address.addr = y
			nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S') #�ɼ�
			address.rdate = nowDatetime #�ɼ�
			address.save()
			return HttpResponseRedirect(reverse('list'))


		cf) ���������� Ȯ��
			http://127.0.0.1:8000/soosapp/list


[ 'Part2' ] ���� ���� # 07-28�� ����

'soosapp/views.py'�� 'def list(request):' �ȿ��� �׽���

1. WHERE
	#addresses =  Address.objects.all().values()
    addresses =  Address.objects.filter(name='ȫ�浿').values() # ���ϴ� ������ �Ǵ�

	#���) select * from ADDRESS where name='ȫ�浿' <- ������ �Ŵ� ������ó�� ������ �ɾ ���

2. AND
	addresses =  Address.objects.filter(name='ȫ�浿', addr='�����').values() 

	#���) select * from ADDRESS where name='ȫ�浿' and ADDR='�����'	

3. OR
	
	addresses =  Address.objects.filter(name='ȫ�浿').values() | Address.objects.filter(addr='�����').values()

	�Ǵ�

	from django.db.models import Q # ��������ߴ�!
	... 
	addresses =  Address.objects.filter(Q(name='ȫ�浿') | Q(addr='�����')).values()

	#���) select * from ADDRESS where NAME='ȫ�浿' or ADDR='�����'

4. FIELD LOOKUP 
	addresses =  Address.objects.filter(name__startswith='��')

    �Ǵ� 

	addresses =  Address.objects.filter(name__startswith='��').values()


	#���) select * from ADDRESS where NAME like '��%'

	cf) __XXX Ű����
		Ű���� ��		����
		contains	Contains the phrase #������ �� �ִ��� Ȯ��, ���ڿ� ���Կ��� Ȯ��
		icontains	Same as contains, but case-insensitive #������ �� �ִ��� Ȯ��, ���ڿ� ���Կ��� Ȯ�� ������ ��ҹ��ڸ� ���� X
		date	    Matches a date #��ü�� ��¥,�ð��� ǥ��
		day	        Matches a date (day of month, 1-31) (for dates) # ��¥���� ('��',1-31)�� ǥ��
		endswith	Ends with #���ڿ��� ������ ���̻�(���� �����ϴ� �ܾ�)�� ������ ���θ� Ȯ���ϴ� �� ���
		iendswith	Same as endswidth, but case-insensitive # endswith �� ���� �������� ��ҹ��ڸ� �������� �ʴ´�.
		exact	    An exact match # ��Ȯ�� ��ġ�ϴ� ���ڿ��� ã�´�.
		iexact	    Same as exact, but case-insensitive # exact �� ������ ��ҹ��ڸ� �������� �ʴ´�.
		in	        Matches one of the values # ������ �� �� �ϳ��� ��ġ�ϸ� ���� ��ȯ�Ͽ� �ش�.
		isnull	    Matches NULL values # null=(������)�� ǥ���� ���� Ture ������ ��ȯ���� �ش�.
		gt	        Greater than # DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ���� ŭ, <
		gte	        Greater than, or equal to # DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ���� ũ�ų� ����, <= ,ge�� ǥ��
		hour	    Matches an hour (for datetimes) #�ð����� '��'�� ǥ��
		lt	        Less than # DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ���� ����, >
		lte	        Less than, or equal to # DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ���� �۰ų� ����, >= ,le�� ǥ��
		minute	    Matches a minute (for datetimes) # �ð����� '��'�� ǥ��
		month	    Matches a month (for dates) # ��¥���� '��'�� ǥ��
		quarter	    Matches a quarter of the year (1-4) (for dates) # ���� 1~4�б⸦ ǥ������
		range	    Match between # ���ӵ� ����(����) �� ������ִ� �Լ�, x���� x ���� �ȿ� ���Ե� ��� ������ ǥ��
		regex	    Matches a regular expression # ���Խ�, ���ڿ��� ���ϰ� ��ġ�ϴ����� ���� ���� ã�ƺ��� �Լ�, 'import re' �� ���
		# ���Խ��̶�? : �ؽ�Ʈ ������� ���α׷��� ���� ���ڿ��� �˻��� ġȯ�� ���� ����
		iregex	    Same as regex, but case-insensitive # regex�� ������ ��ҹ��ڸ� �������� ����.
		second	    Matches a second (for datetimes) #�ð����� '��'�� ǥ��
		startswith	Starts with #���ڿ��� ������ ���̻�(���� �����ϴ� �ܾ�)�� �����ϴ� ���θ� Ȯ���ϴ� �� ���
		istartswith	Same as startswith, but case-insensitive # startswith �� ������ ��ҹ��ڸ� �������� ����
		time	    Matches a time (for datetimes) # ��ü�� �ð��� ǥ��, 'import time' ���� ���
		week	    Matches a week number (1-53) (for dates) # 1���� '��'�� ǥ���� �ش�.
		week_day	Matches a day of week (1-7) 1 is sunday # ������ ������ ��ȯ�մϴ�. �������� 0�̰� �Ͽ����� 6�Դϴ�
		iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday # ������ ������ ��ȯ�մϴ�. �������� 1�̰� �Ͽ����� 7�Դϴ�
		# ISO 8601 =  ���ڿ��� ���·� �ð��� ǥ���ϴ� ����� ���
		iso_year    Matches an ISO 8601 year (for dates) # ������ '��'�� ǥ��
		eq			# equal, DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ����, == 
		ne			# not equal, DataFrame�� ũ�� �񱳸� �����ϴ� �޼���, ���� ���� , != ,ne�� ǥ��

5. ORDER BY
	(1) ASC
		addresses = Address.objects.all().order_by('name').values()

		#���) select * from ADDRESS order by NAME

	(2) DESC  
		addresses =  Address.objects.all().order_by('-name').values() #desc�� - �� ǥ��!

		#���) select * from ADDRESS order by NAME

	(3) �������� ORDER BY 
		addresses =  Address.objects.all().order_by('-name', 'addr', '-id').values()
		
		#���) select * from ADDRESS order by NAME desc, ADDR asc, ID desc

# 07 29 ���� ���� �̰� �ſ� �߿���!!

[ 'Part3' ] ���� (Session)
1. ����( Models	)
	(1) soosapp/models.py�� �߰� 
		...
		class Member(models.Model):
			name = models.CharField(max_length=30)
			email = models.TextField(primary_key=True) #id�ʵ尡 ���� �������� �ʰ� ��
			pwd = models.CharField(max_length=30)
			phone = models.CharField(max_length=50)
			rdate = models.DateTimeField()
			udate = models.DateTimeField()

	(2) soosapp/migrations ��ɾ�� ���� 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py makemigrations soosapp
		#���) soosapp\migrations\0003_member.py ����Ȯ�� ( Create model Member �� )

	(3) ���� (���̱׷�Ʈ) 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py migrate
		#���) Applying soosapp.0003_member... OK ( SQLite DBMS�� ���� �� ) 

	(4) ������ ����� MySQL�� SQL�� �Ʒ��� ���� 
		create table Member (
			name varchar(30), 
			email varchar(50) primary key, 
			pwd varchar(30),
			phone varchar(50),
			rdate datetime, 
			udate datetime	
		);

	(5) DB���̺� ������ ����
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py shell

		>>> from soosapp.models import Member
		>>> Member.objects.all()

		>>> from django.utils import timezone
		>>> nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
		>>> member = Member(name='ȫ�浿', email='hong@hanmail.net', pwd='1234', phone='0101231234', rdate=nowDatetime, udate=nowDatetime)
		>>> member.save()
		>>> member = Member(name='�̼���', email='lee@hanmail.net', pwd='1234', phone='0101231235', rdate=nowDatetime, udate=nowDatetime)
		>>> member.save()
		>>> Member.objects.all().values()


2. login 
	(1) templates/login.html ���� 
		...
		{% load static %}
		<script src="{% static '/js/trim.js' %}"></script>
		...
		<form name="f" action="login_ok/" method="post">
        {% csrf_token %}
		...

	(2) soosapp/views.py
		from django.shortcuts import redirect, render #���2
		def login(request):
			#template = loader.get_template('login.html') #���1
			#return HttpResponse(template.render({}, request)) #���1
			return render(request,'login.html') #���2 

	(3) soosapp/urls.py 
		path('login/', views.login, name='login'), #�߰�

	(4) templates/index.html 
		<a href="login">�α���</a>

	(5) �׽�Ʈ
		1) �������� 
			(env_django) C:\SOO\PyDjango\pj_django>py manage.py runserver 
	
		2) ȣ�� 
			http://127.0.0.1:8000/soosapp/

3. login_ok
	(1) soosapp/urls.py
		path('login/login_ok/', views.login_ok, name='login_ok'), #�߰�

	(2) soosapp/views.py
		from .models import Member
		def login_ok(request):
			#email = request.POST['email'] #���1
			#pwd = request.POST['pwd'] #���1
			email = request.POST.get('email', None) #���2
			pwd = request.POST.get('pwd', None) #���2
			print("email", email, "pwd", pwd)
			
			try:
				member = Member.objects.get(email=email)
			except Member.DoesNotExist:
				member = None
			print("member", member)
			
			result = 0
			if member != None:
				print("�ش� emailȸ�� ������")
				if member.pwd == pwd:
					print("��й�ȣ���� ��ġ") 
					result = 2
					
					print("member.email", member.email) #���1
					request.session['login_ok_user'] = member.email #���1
					
					#session_id = request.session.session_key #���2
					#print("session_id", session_id) #���2
					#request.session['login_ok_user'] = session_id #���2
				else:
					print("��й�ȣ Ʋ��")
					result = 1
			else:
				print("�ش� emailȸ�� �������� ����") 
				result = 0   
			
			temlate = loader.get_template("login_ok.html")
			context = {
				'result': result, 
			}
			return HttpResponse(temlate.render(context, request))

	
	(3) templates/login_ok.html ����
		<script language="javascript">
			//alert({{result}});

			/*
			if({{result}} == 0){
				alert("�α����!! (ȸ�� ���̵� �������� ����)");
			}else if({{result}} == 1){
				alert("�α����!! (��й�ȣ�� Ʋ��)");
			}else{
				alert("�α伺��!!");    
			}
			*/

			switch({{result}}){
				case 0:
					alert("�α����!! (ȸ�� ���̵� �������� ����)");
					break;
				case 1:
					alert("�α����!! (��й�ȣ�� Ʋ��)");
					break;
				case 2:
					alert("�α伺��!!");
			}
			location.href = "../../"
		</script>

	(4) pj_django/pj_django/settings.py �� �߰�
		TEMPLATE_CONTEXT_PROCESSORS = (
			'django.core.context_processors.request',
		)

	    #cf) Ȯ��!! 
		def index(request):
			temlate = loader.get_template('index.html')
			#return HttpResponse(temlate.render()) # ���߿� session�������� �������� ����
			return HttpResponse(temlate.render({}, request)) #������ ����Ϸ���.. request�� �Ѱ���� ��

	
	(5) templates/index.html ���� 
		<!-- login_ok_user: {{request.session.login_ok_user}} --> 

		{% if request.session.login_ok_user %}
			<a href="logout">�α׾ƿ�</a>
		{% else %}
			<a href="login">�α���</a>
		{% endif %}

4. logout
	(1) soosapp/urls.py
		path('logout/', views.logout, name='logout'), #�߰�

	(2) soosapp/views.py
		def logout(request):
			if request.session.get('login_ok_user'):
				#request.session.clear() # �������� �ش� user�� session���� �ʱ�ȭ
				request.session.flush() # �������� �ش� user�� session���� ����
			return redirect("../")
		
		
['Part4'] ########## ������� ###############