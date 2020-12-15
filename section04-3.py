# section04-3
# requests
# requests 사용 스크랩핑(3) - Rest API

# Rest API : GET, POST, DELETE, PUT:UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# 중요 : url을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET : www.movies.com/movies : 영화를 전부 조회
# GET : www.movies.com/movies/: id : 아이디인 영화를 조회
# POST : www.movies.com/movies/ : 영화를 생성
# PUT :  www.movies.com/movies/ : 영화를 수정
# DELETE :  www.movies.com/movies/ : 영화를 삭제

# 세션 활성화
# 예제1
import requests
s = requests.Session()

r = s.get('https://api.github.com/events')

# 수신상태 체크
r.raise_for_status()

# 출력
# print(r.text)

# 예제
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'niceman', domain="httpbin.org", path='/cookies')

r = s.get('https://httpbin.org/cookies', cookies=jar)

print(r.text)

r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)

# 예제4
r = s.post('http://httpbin.org/post',
           data={'id': 'text', 'pw': '111'}, cookies=jar)
print(r.text)


# 예제 5
# 요청(post)
payload1 = {'id': 'text', 'pw': '111'}
payload2 = (('id', 'text'), ('pw', '11111'))
r = s.post('http://httpbin.org/post', data=payload2)

print(r.text)

# 예제 6
r = s.put('http://httpbin.org/put', data=payload1)
print(r.text)

# 예제 7
r = s.delete('http://httpbin.org/delete')
print(r.text)
