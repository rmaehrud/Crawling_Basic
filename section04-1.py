# section 04
# requests
# 스크립팽(1) - session

# 세션 활성화
import requests

s= requests.Session()
# r= s.get('https://www.naver.com')

# # 수신 데이터
# print(r.text)

# # 수신 상태 코드
# print('status code : {}'.format(r.status_code))


# print('ok? : {}'.format(r.ok))

# 세션 종료 불필요한 리소스 차단
s.close()

# 쿠키 리턴 http://httpbin.org/ 이런 사이트에서 연습가능

s = requests.Session()

r1 = s.get('http://httpbin.org/cookies', cookies={'name':'kim1'})
print(r1.text)

# 쿠키 set 저장하는 메소드
r2 = s.get('http://httpbin.org/cookies/set', cookies={'name':'kim2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': 'nice-man_1.0.0_win10_ram16_home__chrome'}

#header 정보 전송
r3 = s.get(url,headers=headers,cookies={'name':'kim2'})
print(r3.text)

# 세션 비활성화
s.close()

# with문 권장 -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
    s.close()

