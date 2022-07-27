[ 'Part1' ] CRUD

1. 환경셋팅
	(1) 버젼 확인
		1) $ python --version
		20 $ pip --version

	(2) 가상 환경(해당 폴더에만 적용되는 가상환경설정 가능)
		

		[파이썬 자체에서 생성하는 방법]
		1) 생성
			$ py -m venv env_django
			또는 
			$ python -m venv env_django

			#참고) 아나콘다에서 생성
			$conda create -n env_django python=3.9.6

		2) 활성화
			$ env_django\Scripts\activate.bat

			#참고1) $ env_django\Scripts\deactivate.bat #비활성화 
			#참고2) 아나콘다에서 활성화
			$conda activate env_django
	
	(3) 장고 셋팅
		1) 인스톨
			(env_django) C:\SOO\PyDjango> py -m pip install Django
			또는 
			(env_django) C:\SOO\PyDjango> python -m pip install Django


			#참고) 필요하면 pip 업그레이드 
			(env_django) C:\SOO\PyDjango> py -m pip install --upgrade pip
		
		2) 버젼확인
			(env_django) C:\SOO\PyDjango> django-admin --version 

	(4) 프로젝트 ( 'pj_django' ) 
		1) 생성 
			(env_django) C:\SOO\PyDjango> django-admin startproject pj_django

		2) 실행
			(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		3) 브라우저에서 확인 ( python cmd에서 나오는 링크를 클릭하면된다.)
			http://127.0.0.1:8000/

	(5) 앱 ( 'soosapp' )
		1) 서버정지 
			플젝 실행중이라면 정지시킴 ( Ctrl + C )

		2) 생성
			(env_django) C:\SOO\PyDjango\pj_django> py manage.py startapp soosapp

2. 뷰즈 ( Views )
	(1) soosapp/views.py
	from django.http import HttpResponse
	from django.shortcuts import render

	def index(request):
		return HttpResponse("안녕 장고^^")
	
	(2) soosapp/urls.py 생성 및 편집 
		from django.urls import path
		from . import views

		urlpatterns = [
			path('', views.index, name='index'),
		]
		
	(3) pj_django/pj_django/urls.py 편집 
		from django.contrib import admin
		from django.urls import path
		from django.urls import include, path

		urlpatterns = [
			path('admin/', admin.site.urls),
			path('soosapp/', include('soosapp.urls')),
		]

	(4) 서버실행 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/

3. 탬플릿츠( Templates	 ) 
	(1) soosapp/templates/index.html 구조 생성 (폴더+파일) 
		<!DOCTYPE html>
		<center>
			<h1>Soo's index.html</h1>
		</center>

	(2) soosapp/views.py 수정 
		...
		from django.template import loader

		def index(request):
			temlate = loader.get_template('index.html')
			return HttpResponse(temlate.render())

	(3) pj_django/pj_django/settings.py 수정 
		INSTALLED_APPS = [
			...
			'soosapp.apps.SoosappConfig' #이부분 추가
		]
		
	(4) 적용 (마이그레트)  
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py migrate
			
	(5) 서버실행 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/ 	

4. 모델즈( Models	) 
	(1) soosapp/models.py
		from django.db import models

		class Address(models.Model):
			name = models.CharField(max_length=200)
			addr = models.TextField()
			rdate = models.DateTimeField()

	(2) soosapp/migrations 명령어로 생성 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py makemigrations soosapp

		#결과) migrations/0001_initial.py 생성확인 ( Create model Address 됨 ) 

	(3) 적용 (마이그레트) 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py migrate

		#결과) Applying soosapp.0001_initial.py 실행 ( SQLite DBMS에 적용 됨 ) 

	(4) 위에서 실행된 MySQL의 SQL은 아래와 같음 
		create table Address (
			id int primary key autoincrement,
			name varchar(200), 
			addr text,
			rdate datetime
		);
		
5. DB테이블에 데이터 삽입 
	(1) Python shell 창 열기 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py shell

		#종료) >>> quit()

	(2) Record 추가
	    0) timezone 변경 ( pj_django/pj_django/settings.py 를 수정 )
			#TIME_ZONE = 'UTC'
			TIME_ZONE = 'Asia/Seoul'

			#USE_TZ = True
			USE_TZ = False

				
		1) 1개
			<1> 방법1
				>>> from soosapp.models import Address
				>>> Address.objects.all()

				>>> from django.utils import timezone
				>>> print(timezone.now())
				>>> nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
				>>> print(nowDatetime)
				>>> address = Address(name='홍길동', addr='서울시', rdate=nowDatetime)
				>>> address.save()

				>>> Address.objects.all().values()

			<2> 방법2
				>>> import datetime
				>>> now = datetime.datetime.now()
				>>> print(now)
				>>> nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
				>>> print(nowDatetime)
				>>> address = Address(name='강감찬', addr='인천시', rdate=nowDatetime)
				>>> address.save()

				>>> Address.objects.all().values()

		2) N개 
			>>> address1 = Address(name='이순신', addr='부산시', rdate=nowDatetime)
			>>> address2 = Address(name='유관순', addr='광주시', rdate=nowDatetime)
			>>> address3 = Address(name='을지문덕', addr='대전시', rdate=nowDatetime)
			>>> address_list = [address1, address2, address3]
			>>> for x in address_list:
					x.save()
		    
			>>> Address.objects.all().values()

	(3) Record 삭제 
		1) 1개 
			>>> address = Address.objects.get(id=2)
			>>> address.delete()

		2) N개
			>>> addresses = Address.objects.all()
			>>> addresses.delete()

		3) 확인 
			>>> Address.objects.all().values()


6. 'R'ead 			
	(1) soosapp/views.py 에 추가
		...
		from .models import Address

		def list(request):
			temlate = loader.get_template('list.html')
			addresses =  Address.objects.all().values()
			context = {
				'addresses': addresses, 
			}
			return HttpResponse(temlate.render(context, request))
		
	(2) soosapp/templates/list.html 생성 및 수정
		<a href='../'>인덱스</a><br/>
	    ... 
		{% for address in addresses %}
		<tr>
		<td align='center'>{{address.id}}</td>
		<td>{{address.name}}</td>
		<td>{{address.addr}}</td>
		<td>{{address.rdate}}</td>
		<td align='center'><a href="">삭제</a></td>
		</tr>
		{% endfor %}
		...

	(3) soosapp/urls.py 에 추가
		path('list/', views.list, name='list'), #추가

	(4) 서버실행 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/list  

	(5) soosapp/templates/index.html 에 링크 추가 
		<a href="list">회원</a><br/>


7. 'C'reate ####### 점심 먹고 ######
	(1) soosapp/templates/list.html 에서 링크 수정
	    ...
		<a href='../write'>입력</a>  
		...

	(2) soosapp/templates/write.html 생성 
		...
		<form name="f" action="write_ok" method="post">
           {% csrf_token %}
		...
'''
	(3) soosapp/templates/js/trim.js 생성  #문제 있음 # 다시 알아보기 4:15~
		function trim(str){
			while(str && str.indexOf(" ") == 0)
				str = str.substring(1); 
			while(str && str.lastIndexOf(" ") == str.length-1)
				str = str.substring(0, str.length-1); 
			return str;
		}
'''
	(3) static 폴더생성 및 셋팅 ( for 'trim.js' )
		<1> pj_django/pj_django/settings.py 확인
			# Static files (CSS, JavaScript, Images)
			STATIC_URL = 'static/'

		<2> soosapp/static 폴더 생성 / 그 하위 폴더들 생성 
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

	(4) soosapp/views.py 에 추가 
		def write(request):
			temlate = loader.get_template('write.html')
			return HttpResponse(temlate.render())

	(5) soosapp/urls.py 에 추가
		path('write/', views.write, name='write'), #추가

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/

	(6) soosapp/urls.py 에 추가2
		path('write/write_ok/', views.write_ok, name='write_ok'), #추가

	(7) soosapp/views.py 에 추가2
		from django.urls import reverse 
		from django.utils import timezone
		def write_ok(request):
			x = request.POST['name']
			y = request.POST['addr']
			nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
			address = Address(name=x, addr=y, rdate=nowDatetime)
			address.save()
			return HttpResponseRedirect(reverse('list'))

	(8) 서버실행 
		(env_django) C:\SOO\PyDjango\pj_django> py manage.py runserver

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/write
		

8. 'D'elete
	(1) soosapp/templates/list.html 수정
		...
		<td align='center'><a href="../delete/{{address.id}}">삭제</a></td> 
		... 

		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/list 에서 '삭제'에 마우스오버

	(2) soosapp/urls.py 에 추가
		path('delete/<int:id>', views.delete, name='delete'), #추가

	(3) soosapp/views.py 에 추가 
		def delete(request, id):
			address = Address.objects.get(id=id)
			address.delete()
			return HttpResponseRedirect(reverse('list'))


		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/list

9. 'U'pdate # 미션
	(1) soosapp/templates/list.html 수정
		...
		<td align='center'><a href="../update/{{address.id}}">{{address.id}}</a></td>
		...

	(2) soosapp/urls.py 에 추가1
		path('update/<int:id>', views.update, name='update'), #추가

	(3) soosapp/templates/update.html 생성 및 수정
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

	(4) soosapp/views.py 에 추가1 
		def update(request, id):
			temlate = loader.get_template('update.html')
			address = Address.objects.get(id=id)
			context = {
				'address': address, 
			}
			return HttpResponse(temlate.render(context, request))


		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/list

	
	(5) soosapp/urls.py 에 추가2
		path('update/update_ok/<int:id>', views.update_ok, name='update_ok'), #추가

	(6) soosapp/views.py 에 추가2
		def update_ok(request, id):
			x = request.POST['name']
			y = request.POST['addr']
			address = Address.objects.get(id=id)
			address.name = x
			address.addr = y
			nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S') #옵션
			address.rdate = nowDatetime #옵션
			address.save()
			return HttpResponseRedirect(reverse('list'))


		cf) 브라우져에서 확인
			http://127.0.0.1:8000/soosapp/list


[ 'Part2' ] ######## 복습 ########
		