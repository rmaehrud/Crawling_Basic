# Section03-2
# 기본 스크랩핑 실습
# GET 방식 데이터 통신(2) - RSS

import urllib.request
import urllib.parse # 일반형태로 변경
#https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
#https://www.mois.go.kr/

# 행정 안전부
API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'
params = []

for num in [1001,1002,1012,1014]:
    params.append(dict(ctxCd=num))

# 연속해서 4회 요청
for c in params:
    #피라미터 출력
    # URL 인코딩
    param = urllib.parse.urlencode(c) #url로 인코딩한다
    url = API + "?" + param
    #url 출력
    print('url : {}'.format(url))

    # 요청
    res_data=urllib.request.urlopen(url).read()# url 정보를 읽는다
    req=res_data.decode('UTF-8') # 데이타 디코드
    print(req)