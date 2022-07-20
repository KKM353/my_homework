1. Numpy 
	(0) 가상환경생성
		conda create -n env_pyadvanced python=3.9.6

	(1) 인스톨 넘파이 
		pip install numpy
	
	(2) NumPy의 데이터타입 
	    i - integer
		b - boolean
		u - unsigned integer
		f - float
		c - complex float
		m - timedelta
		M - datetime
		O - object
		S - string
		U - unicode string
		V - other type 

		(참고) Python 데이터타입
		- Text: str
		- Numeric: int, float, complex 
		- Sequence: list, tuple, range
		- Mapping: dict 
		- Set: set, frozenset 
		- Boolean: bool
		- Binary: bytes, bytearray, memoryview

	(3) 인스톨 씨본&맷플로트 
		pip install seaborn
		#pip install matplotlib

2. Pandas 
    (0) 데이터셋(data set)의 분석, 정제, 탐색, 조작 lib

    (1) 인스톨 넘파이 
		pip install pandas
        
    (2) 인스톨 
	    pip install openpyxl
		pip install lxml

	(3) 데이터 정제
		1) 일반화값 
		    <1> median ( mid point value )
			<2> mean ( average value )
			<3> mode ( most common value ) 

			예) 1  3  2  5  1
			   - median: 3 (중앙값)
			   - mean: 2.4 (평균)
			   - mode: 1 (가장일반적)

		2) Empty 표현 
		    <1> NA(Not Available)
			<2> NaN(Not a Number)  
			<3> NaT(Not a Time) 
			<4> None ( 파이썬에는 null이 없음 )
		
		3) inplace=True 옵션 
		    새로운 df를 리턴하지않고, 원본df(Original DataFrame)에 직접 적용 

		4) 상관관계계수( Correlations )
		   - x = df.corr()
		   - x범위: -1 ~ 1 
		   - 한 변수가 '증가'할 때 다른 변수는 '감소'하는 경향이 있으면 계수는 '음수'
           
	(4) 인스톨 맷플로트 
		pip install matplotlib

3. Matplotlib
	(1) 마커 
		1) 모양 
			'o'	Circle	
			'*'	Star	
			'.'	Point	
			','	Pixel	
			'x'	X	
			'X'	X (filled)	
			'+'	Plus	
			'P'	Plus (filled)	
			's'	Square	
			'D'	Diamond	
			'd'	Diamond (thin)	
			'p'	Pentagon	
			'H'	Hexagon	
			'h'	Hexagon	
			'v'	Triangle Down	
			'^'	Triangle Up	
			'<'	Triangle Left	
			'>'	Triangle Right	
			'1'	Tri Down	
			'2'	Tri Up	
			'3'	Tri Left	
			'4'	Tri Right	
			'|'	Vline	
			'_'	Hline

		2) 컬러 
			'r'	Red	
			'g'	Green	
			'b'	Blue	
			'c'	Cyan	
			'm'	Magenta	
			'y'	Yellow	
			'k'	Black	
			'w'	White

			cf) colorpicker : 임의색 지정가능

		3) 라인
			'-'	Solid line	
			':'	Dotted line	
			'--' Dashed line	
			'-.' Dashed/dotted line	

	(2) 마커 약자 
	    1) ms ( marker size ) 
		2) mec ( markeredgecolor ) 
		3) mfc ( markerfacecolor )

	(2) 라인차트 ( D.py )

	(3) 레이블 ( E.py )

	(4) 배치레이아웃과 위치지정 ( F.py )
		- subplot()으로

	(4) 스케터 ( G.py )
	    cf) 컬러맵스 ( ColorMaps ) 
		Accent		 	Accent_r	
		Blues		 	Blues_r	
		BrBG		 	BrBG_r	
		BuGn		 	BuGn_r	
		BuPu		 	BuPu_r	
		CMRmap		 	CMRmap_r	
		Dark2		 	Dark2_r	
		GnBu		 	GnBu_r	
		Greens		 	Greens_r	
		Greys		 	Greys_r	
		OrRd		 	OrRd_r	
		Oranges		 	Oranges_r	
		PRGn		 	PRGn_r	
		Paired		 	Paired_r	
		Pastel1		 	Pastel1_r	
		Pastel2		 	Pastel2_r	
		PiYG		 	PiYG_r	
		PuBu		 	PuBu_r	
		PuBuGn		 	PuBuGn_r	
		PuOr		 	PuOr_r	
		PuRd		 	PuRd_r	
		Purples		 	Purples_r	
		RdBu		 	RdBu_r	
		RdGy		 	RdGy_r	
		RdPu		 	RdPu_r	
		RdYlBu		 	RdYlBu_r	
		RdYlGn		 	RdYlGn_r	
		Reds		 	Reds_r	
		Set1		 	Set1_r	
		Set2		 	Set2_r	
		Set3		 	Set3_r	
		Spectral		Spectral_r	
		Wistia		 	Wistia_r	
		YlGn		 	YlGn_r	
		YlGnBu		 	YlGnBu_r	
		YlOrBr		 	YlOrBr_r	
		YlOrRd		 	YlOrRd_r	
		afmhot		 	afmhot_r	
		autumn		 	autumn_r	
		binary		 	binary_r	
		bone		 	bone_r	
		brg		 	    brg_r	
		bwr		 	    bwr_r	
		cividis		 	cividis_r	
		cool		 	cool_r	
		coolwarm		coolwarm_r	
		copper		 	copper_r	
		cubehelix		cubehelix_r	
		flag		 	flag_r	
		gist_earth		gist_earth_r	
		gist_gray		gist_gray_r	
		gist_heat		gist_heat_r	
		gist_ncar		gist_ncar_r	
		gist_rainbow	gist_rainbow_r	
		gist_stern		gist_stern_r	
		gist_yarg		gist_yarg_r	
		gnuplot		 	gnuplot_r	
		gnuplot2		gnuplot2_r	
		gray		 	gray_r	
		hot		 	    hot_r	
		hsv		 	    hsv_r	
		inferno		 	inferno_r	
		jet		 	    jet_r	
		magma		 	magma_r	
		nipy_spectral	nipy_spectral_r	
		ocean		 	ocean_r	
		pink		 	pink_r	
		plasma		 	plasma_r	
		prism		 	prism_r	
		rainbow		 	rainbow_r	
		seismic		 	seismic_r	
		spring		 	spring_r	
		summer		 	summer_r	
		tab10		 	tab10_r	
		tab20		 	tab20_r	
		tab20b		 	tab20b_r	
		tab20c		 	tab20c_r	
		terrain		 	terrain_r	
		twilight		twilight_r	
		twilight_shifted		twilight_shifted_r	
		'viridis'		viridis_r	
		winter		 	winter_r

	(6) 바차트 ( H.py )	
	
	(7) 히스토그램 ( I.py )
		
	(8) 파이차트 ( J.py )

	
4. AI (Artificial Intelligence) #정확한 것은 아니니 스스로 공부를 더 해야된다.
    (0) AI 개요 
	    1) 스스로 '판단'하고 '예측'하는 알고리즘 
		2) 일반프로그램과 차이점 
           <1> 일반 프로그램 
			   알고리즘 + 데이터 => '결과'
		   <2> AI
				데이터 + 결과 => '알고리즘'

		3) AI포함관계 
		   약(Weak:'simulate'(인간의 지식을 모방)) < 머신러닝 < 딥러닝(NN) < 강(String:'copy'(인간의 지능을 복사)) #점점 진화중이다.

		4) NN(Neural Networks)
			<1> 신경망(데이터 레이어)
			<2> 종류 
			   - DNN ( Deep Neural Network )
			   - CNN ( Convolutional Neural Network )
			   - RNN ( Recurrent Neural Network )

				cf) Google이 인수해서 대박친 회사 Top3
					- 딥마인드 (개발자 : 데미스 하사비스 )
					- 유튜브
					- 안드로이드

		5) 일반적인 기능  
			말하기 / 생각하기 / 학습하기 / 계획짜기 / 이해하기

	    6) pip install sklearn

	(2) Data Samples  
		4SD
		s = [87,88,89,87,88,86,87]
		s = [33,112,139,29,60,78,98] 
		
		4P
		a = [6,32,44,49,51,42,8,12,16,40,81,83,33,3,9,7,26,37,28,62,32]
	
	    4L
		x = [6,8,9,8,3,18,3,10,5,12,13,10,7]
		y = [100,87,88,89,112,87,104,88,95,79,78,86,87]

		x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
		y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]

        4P
		x = [2,3,4,6,7,8,9,10,11,13,14,15,16,17,19,20,22,23]
		y = [101,91,81,61,61,56,61,66,71,71,76,77,79,80,91,100,100,101]

		x = [90,44,37,37,96,11,67,35,39,21,27,30,49,65,7,6,37,67,73,41]
		y = [22,47,4,36,68,96,54,73,59,11,27,35,91,34,39,21,57,3,48,16]


5. pymongo
	(1) mongodb 
	    1) 다운로드 
			https://www.mongodb.com/try/download/community
			https://www.mongodb.com/try/download/enterprise

			(설치블로그)  
			https://khj93.tistory.com/entry/MongoDB-Window%EC%97%90-MongoDB-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
		
		2) 환경변수 추가
		   Path => C:\Program Files\MongoDB\Server\5.0\bin

		3) 버젼 확인 
		   $> mongo --version

	(2) 파이몽고 설치 
		python -m pip install pymongo

		cf) 현재날짜가져오기
		https://ponyozzang.tistory.com/627
# 07 19 수업내용
	(3) 입력데이터 
		dics = [
		  { "name": "가길동", "addr": "서울", "rdate":dt_now},
		  { "name": "나길동", "addr": "경기", "rdate":dt_now},
		  { "name": "다길동", "addr": "부산", "rdate":dt_now},
		  { "name": "라길동", "addr": "인천", "rdate":dt_now},
		  { "name": "마길동", "addr": "대구", "rdate":dt_now},
		  { "name": "바길동", "addr": "광주", "rdate":dt_now},
		  { "name": "사길동", "addr": "대전", "rdate":dt_now},
		  { "name": "아길동", "addr": "울산", "rdate":dt_now},
		  { "name": "자길동", "addr": "창원", "rdate":dt_now},
		  { "name": "차길동", "addr": "청주", "rdate":dt_now}
		]
		dics = [
		  { "_id":1, "name": "가길동", "addr": "서울", "rdate":dt_now},
		  { "_id":2, "name": "나길동", "addr": "경기", "rdate":dt_now},
		  { "_id":3, "name": "다길동", "addr": "부산", "rdate":dt_now},
		  { "_id":4, "name": "라길동", "addr": "인천", "rdate":dt_now},
		  { "_id":5, "name": "마길동", "addr": "대구", "rdate":dt_now},
		  { "_id":6, "name": "바길동", "addr": "광주", "rdate":dt_now},
		  { "_id":7, "name": "사길동", "addr": "대전", "rdate":dt_now},
		  { "_id":8, "name": "아길동", "addr": "울산", "rdate":dt_now},
		  { "_id":9, "name": "자길동", "addr": "창원", "rdate":dt_now},
		  { "_id":10, "name": "차길동", "addr": "청주", "rdate":dt_now}
		]

6. Crawling
	(1) BeautifulSoup
		1) 패키지 설치 
			(env_pyadvanced) C:\SOO\PyAdvanced\day06_crawling>pip install bs4

		2) API 
		    https://www.crummy.com/software/BeautifulSoup/bs4/doc/

		3) HTML샘플분석 ( 'A.py' )
		   
			
		4) 네이버 requests ( 'B.py' ) 
			(env_pyadvanced) C:\SOO\PyAdvanced\day06_crawling>pip install requests 

		5) 네이트 실시간 ( 'C.py' ) 
			<1> URL 
				https://www.nate.com/

			<2> 선택자 지정 
				https://www.nate.com/ -> F12 -> 개발자모드 왼쪽 상단의 Select 이이콘 '클릭' 
				-> 웹브라우져상에서 크롤링할 대상 '클릭' -> 개발자모드의 Elements탭 확성화라인에 '우클릭'
				-> Copy -> Copy Selector 

			<3> 메모장 붙여넣기 
			    #olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank

		6) 주식 데이터 크롤링 ( 'D.py' )
		   
				    
	(2) Selenium		    
		1) 환경설정 
			<1> (env_crawling) C:\~>pip install selenium
			<2> Web Driver 다운/설치 
				1> 크롬 버젼 확인 
					( 메뉴 -> 도움말 -> Chrome정보 ) #크롬버젼: 103.0.5060.134
				2> chromedriver_win32.zip 다운 
					( https://chromedriver.chromium.org/downloads )  #드라이버버젼:103.0.5060.53
				3> 설치 
					chromedriver.exe
				4> Code 실행 

		2) 구글검색어 테스트 ( 'F.py' )

		3) 페이북로그인 테스트 ( 'G.py' )
		    <1> 로긴폼의 email input 에 오른쪽 마우스 -> '검사' 
			<2> 만약.. 바로 꺼진다면.. chromedriver.exe 버젼과 크롬버젼이 맞지 않는 거임
		
		4) 구글 이미지 다운로드 
		    <1> 1개 이미지 다운로드 ( 'H.py' ) 
			<2> n개 이미지 다운로드 ( 'I.py') : 45개 
			<3> 스크롤 다운하면서 n개 이미지 다운로드 ( 'J.py' ) : 45개 초과 
			<4> Xpath이용 이미지 다운로드 ( 'K.py' ) : 45개 초과
				1> '검사 -> Copy -> Copy full XPath' 

				2> 코드 적용 
				    # (1) 변경 로직 
				    #el_img_big = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb") #이전 방법 
					el_img_big = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img")


					# (2) 추가 로직 
					opener=urllib.request.build_opener()
					opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
					urllib.request.install_opener(opener)


	(3) Scrapy 
		1) lib 설치 
			(env_pyadvanced) C:\~>pip install scrapy

		2) Scrapy shell 
			<1> shell 실행 
				(env_pyadvanced) C:\~>scrapy shell 
			<2> Starting Point 지정
			    >>> fetch('http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001')
			<3> 다운로드 된 응답확인 
				>>> view(response)
			<4> html출력 
				>>> print(response.text)
			<5> 뉴스 제목 링크에서 Xpath 추출 
				//*[@id="main_content"]/div[2]/ul[1]/li[1]/dl/dt[2]/a
				//*[@id="main_content"]/div[2]/ul[1]/li[2]/dl/dt[2]/a
				//*[@id="main_content"]/div[2]/ul[1]/li[3]/dl/dt[2]/a
				...
				//*[@id="main_content"]/div[2]/ul[2]/li[6]/dl/dt[2]/a
				//*[@id="main_content"]/div[2]/ul[2]/li[7]/dl/dt[2]/a
			<6> Xpath 일반화 
				//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a
            <7> 뉴스 제목들 확인 
				>>> response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a').extract()
			<8> 뉴스 회사들 확인 
			    >>> response.css('.writing::text').extract()
			<9> 뉴스 내용 미리보기(앞부분) 확인 
				>>> response.css('.lede::text').extract()
		
		3) Scrapy project 
			<1> 플젝 생성 
				(env_pyadvanced) C:\~>scrapy startproject naverscraper
			<2> spiders 폴더에 들어감 
				(env_pyadvanced) C:\SOO\PyAdvanced\day06_crawling\naverscraper\naverscraper\spiders>
			<3> spider('newsbot.py') 생성 
				(env_pyadvanced) C:~\spiders>scrapy genspider newsbot news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001
			<4> 'newsbot.py' 편집 
				import scrapy

				class NewsbotSpider(scrapy.Spider):
					name = 'newsbot'
					start_urls = ['http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001']

					def parse(self, response):
						titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a').extract()
						authors = response.css('.writing::text').extract()
						previews = response.css('.lede::text').extract()
						
						for item in zip(titles, authors, previews):
							scraped_info = {
								'title': item[0].strip(), 
								'author': item[1].strip(), 
								'preview': item[2].strip()
							}
							yield scraped_info


			<5> 'settings.py' 수정
				1> 하단에 추가 
					FEED_FORMAT = "csv"
					FEED_URI = "naver_news.csv"

					FEED_EXPORT_ENCODING="utf-8-sig"

				2> 수정 
					ROBOTSTXT_OBEY = False

			<6> newsbot.py 실행 
				(env_pyadvanced) C:\~\spiders>scrapy crawl newsbot

			<7> 'naver_news.csv'파일에 결과 저장 확인 

-----
넘파이
판다스
맷플롯
AI ( 텐서플로,케라스,파이토치 )
몽고 ( noSql )
크롤링
 <서비스 데이터 준비 >
 1) 주제선정
 2) 데이터채굴 
	- 다운로드 JSON/CSV/EXCEL...
	- 크롤링
 3) 데이터 정제 후 분석/시각화
	- 정제 : 판다스
 4) (옵션) 판단/예측 -> '모델'생성
 5) 서비스를 위한 정제된 데이터 영구저장
	- noSql ( MongoDB )
	- Sql ( Oracle, Mysql, ...)
	- Files ( imgs,json,csv,excel,...)
 6) 추후 '웹 or 앱'으로 서비스