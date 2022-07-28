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


[ 'Part2' ] 질의 집합 # 07-28일 수업

'soosapp/views.py'의 'def list(request):' 안에서 테스팅

1. WHERE
	#addresses =  Address.objects.all().values()
    addresses =  Address.objects.filter(name='홍길동').values() # 원하는 조건을 건다

	#결과) select * from ADDRESS where name='홍길동' <- 조건을 거는 셀렉문처럼 조건을 걸어서 출력

2. AND
	addresses =  Address.objects.filter(name='홍길동', addr='서울시').values() 

	#결과) select * from ADDRESS where name='홍길동' and ADDR='서울시'	

3. OR
	
	addresses =  Address.objects.filter(name='홍길동').values() | Address.objects.filter(addr='서울시').values()

	또는

	from django.db.models import Q # 선언해줘야댐!
	... 
	addresses =  Address.objects.filter(Q(name='홍길동') | Q(addr='서울시')).values()

	#결과) select * from ADDRESS where NAME='홍길동' or ADDR='서울시'

4. FIELD LOOKUP 
	addresses =  Address.objects.filter(name__startswith='이')

    또는 

	addresses =  Address.objects.filter(name__startswith='이').values()


	#결과) select * from ADDRESS where NAME like '이%'

	cf) __XXX 키워드
		키워드 명		설명
		contains	Contains the phrase #문구가 들어가 있는지 확인, 문자열 포함여부 확인
		icontains	Same as contains, but case-insensitive #문구가 들어가 있는지 확인, 문자열 포함여부 확인 하지만 대소문자를 구분 X
		date	    Matches a date #객체의 날짜,시간을 표시
		day	        Matches a date (day of month, 1-31) (for dates) # 날짜에서 ('일',1-31)을 표시
		endswith	Ends with #문자열이 지정된 접미사(내가 지정하는 단어)로 끝나는 여부를 확인하는 데 사용
		iendswith	Same as endswidth, but case-insensitive # endswith 와 같은 뜻이지만 대소문자를 구분하지 않는다.
		exact	    An exact match # 정확히 일치하는 문자열을 찾는다.
		iexact	    Same as exact, but case-insensitive # exact 와 같지만 대소문자를 구분하지 않는다.
		in	        Matches one of the values # 조건의 값 중 하나라도 일치하면 값을 반환하여 준다.
		isnull	    Matches NULL values # null=(결측값)이 표현된 곳은 Ture 값으로 반환시켜 준다.
		gt	        Greater than # DataFrame의 크기 비교를 수행하는 메서드, 보다 큼, <
		gte	        Greater than, or equal to # DataFrame의 크기 비교를 수행하는 메서드, 보다 크거나 같음, <= ,ge로 표기
		hour	    Matches an hour (for datetimes) #시간에서 '시'를 표시
		lt	        Less than # DataFrame의 크기 비교를 수행하는 메서드, 보다 작음, >
		lte	        Less than, or equal to # DataFrame의 크기 비교를 수행하는 메서드, 보다 작거나 같음, >= ,le로 표기
		minute	    Matches a minute (for datetimes) # 시간에서 '분'을 표시
		month	    Matches a month (for dates) # 날짜에서 '달'을 표시
		quarter	    Matches a quarter of the year (1-4) (for dates) # 연중 1~4분기를 표시해줌
		range	    Match between # 연속된 숫자(정수) 를 만들어주는 함수, x에서 x 까지 안에 포함된 모든 정수를 표시
		regex	    Matches a regular expression # 정규식, 문자열이 패턴과 일치하는지에 대한 값을 찾아보는 함수, 'import re' 로 사용
		# 정규식이란? : 텍스트 편집기와 프로그래밍 언어에서 문자열의 검색과 치환을 위해 지원
		iregex	    Same as regex, but case-insensitive # regex와 같지만 대소문자를 구분하지 않음.
		second	    Matches a second (for datetimes) #시간에소 '초'를 표시
		startswith	Starts with #문자열이 지정된 접미사(내가 지정하는 단어)로 시작하는 여부를 확인하는 데 사용
		istartswith	Same as startswith, but case-insensitive # startswith 과 같지만 대소문자를 구분하지 않음
		time	    Matches a time (for datetimes) # 객체의 시간을 표시, 'import time' 으로 사용
		week	    Matches a week number (1-53) (for dates) # 1년을 '주'로 표시해 준다.
		week_day	Matches a day of week (1-7) 1 is sunday # 정수로 요일을 반환합니다. 월요일은 0이고 일요일은 6입니다
		iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday # 정수로 요일을 반환합니다. 월요일은 1이고 일요일은 7입니다
		# ISO 8601 =  문자열의 형태로 시간을 표현하는 방법을 기술
		iso_year    Matches an ISO 8601 year (for dates) # 정수로 '년'을 표기
		eq			# equal, DataFrame의 크기 비교를 수행하는 메서드, 같음, == 
		ne			# not equal, DataFrame의 크기 비교를 수행하는 메서드, 같지 않음 , != ,ne로 표기

5. ORDER BY
	(1) ASC
		addresses = Address.objects.all().order_by('name').values()

		#결과) select * from ADDRESS order by NAME

	(2) DESC  
		addresses =  Address.objects.all().order_by('-name').values() #desc는 - 로 표시!

		#결과) select * from ADDRESS order by NAME

	(3) 여러번의 ORDER BY 
		addresses =  Address.objects.all().order_by('-name', 'addr', '-id').values()
		
		#결과) select * from ADDRESS order by NAME desc, ADDR asc, ID desc

[ 'Part3' ] ##### 여기 부터 #####	