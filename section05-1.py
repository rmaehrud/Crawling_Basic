# section05-1
# Beautifulsoup
# Beautifulsoup 사용 스크랩핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<h1>this is h1 area</h1>
<h2>this is h2 area</h2>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sistes.
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a data-io="link3" href="http://example.com/little" class="brother" id="link3">title</a>
</p>
<p class="story">
syory....
</p>
</body>
</html>
"""

# 예제1(Beautiful soup 기초)
# bs4
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print(h1)

# p 태그 접근
p1 = soup.html.body.p
print(p1)

p2 = p1.next_sibling.next_sibling.next_sibling
print(p2)

# 텍스트 출력1
print('h1 >>', h1.string)

# 텍스트 출력2
print('p >>', p1.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(p2.next_element)

# 반복 출력 확인
# for v in p2.next_element:
#     print(v)

# 예제2(find,find_all)

# bs4 초기화
soup2 = BeautifulSoup(html, 'html.parser')
# 타입 확인
# a 태그 모두 선택
# 중요
link1 = soup2.find_all('a')  # limit=2 옵션2
# 태그안에 속성값 가능
# id="link2", string="title", string
link2 = soup2.find_all('a', class_='brother')
# print(link2)
for t in link1:
    print(t)

# 처음 발견한 a 태그 선택
link3 = soup.find("a")
print()
print(link3)

# 다중 조건
link4 = soup.find("a", {"class": "brother", "data-io": "link3"})
print(link4)
print(link4.text)
print(link4.string)
