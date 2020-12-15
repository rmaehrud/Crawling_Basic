# Section03-1
# 기본 스크랩핑 실습
# GET 방식 데이터 통신(1)

import urllib.request
from urllib.parse import urlparse

# 기본 요청1

url = "http://www.encar.com"

mem = urllib.request.urlopen(url)


# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('parse : {}'.format(urlparse('http://encar.co.kr?test=test').query))


# 기본 요청2()
API = "https://api.ipify.org"

# GET 방식 parameter
values = {
    'format':'jsonp' # text,json
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values) # 딕셔너리 형태가 일반 형태로 바뀜
print('after param : {}'.format(params))

# 요청 url 생성
URL = API + "?" + params
print("요청 url = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read() # url의 들어간 데이터를 읽어줌

text = data.decode('UTF-8') # url의 들어간 데이터를 디코딩
print('response : {}'.format(text))
