# section 04-2
# requests
# requests 사용 스크랩핑(2) - json

import json
import requests

s = requests.Session()

# 100개 json 데이터 요청
r = s.get('http://httpbin.org/stream/100', stream=True)

# 수신 학왼
print(r.text)

# Encoding 확인
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'


print('After Encoding : {}'.format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    print(line)
    print(type(line))

    # json(dict) 변환 후 타입 확인
    b = json.loads(line) # str -> dict
    print(b)
    print(type(b))

    # 정보 내용 출력
    for k, v in b.items():
        print('key : {}, value : {}'.format(k,v))

    print()
    print()

s.close()

# r = s.get("https://jsonplaceholder.typicode.com/todos/1",stream=True)

# # print(r.encoding)
# print(type(r))
# for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line.encoding)
    # print(type(line))


    #  json(dict) 변환 후 타입 확인
    # b = json.loads(line.replace("'", "\""))
    # print(b)
    # print(type(b))



#     b = json.load(line) # str -> dict
#     print(b)
#     print(type(b))


# header 정보

# 본문 정보

# # json 변환
# print(r.json())

# # key 반환
# print(r.json().keys())

# # 인코딩 반환
# print(r.encoding)

# print(r.content)
# print(type(r))
