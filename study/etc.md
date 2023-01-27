# ETC

## 모듈?

> `import module`

* 장점
  * 유지보수 비용(휴먼리소스) 감소

* 단점
  * 모듈.메서드 - DRY원칙 모듈 반복도 원칙에 어긋남

> `import from module import` 메서드

* 장점
  * 모듈 안에 있는 메서드를 사용하기 위한 타이핑 줄어듬
  * 모듈에서 특정 부분만 해당 스크립트에서 접근 가능하도록 제어

* 단점
  * 모듈에서 새로운 항목 추가하려면 import 구문 업데이트 해야함
  * random이라는 모듈에서 `shuffle()` VS `random.shuffle()`
    * 뒤에것이 어디에서 가져왔는지 보임
* 어떤게 좋은지는 맘대로

## 함수 추가

* 파라미터 키워드로 안받고 포지션으로만 받게 할 수 있음

```python
def func1(param1, param2, /): # / 앞에 있는거는 키워드로 못받음
```

## 제이슨 구조 확인

* [제이슨 뷰어](http://jsonviewer.stack.hu/)

## 리퀘스트 모듈 활용 및 예시

* 공식문서 잘 봐서 어떤 데이터 제공하는지 확인하자
  * 뭐가 필수이고 뭐가 옵션인지 알려주기도 함
* 그냥 URL주소 그대로 인터넷에 치면 제이슨으로 나옴

```python
import requests
from pprint import pprint

url = 'https://api.themoviedb.org/3' # 앞쪽 부분

params = { # 필요한 매개변수 직접 설정
    'api_key': '6aee34be99bb1d1b3fa358b709332b7e',
    'language': 'ko'
    #등등.....
}

response = requests.get(url, params=params).json()
pprint(response) # response에 받은 제이슨 파일 출력
```
