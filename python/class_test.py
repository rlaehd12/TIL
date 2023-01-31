## 1. meat 라는 클래스를 한번 정의하고 생각해보자
'''class meat:
    def __init__(self, a, b = 100, *c): # 함수 만들 때 쓰던거 다 먹는듯?
        self.name = a
        self.gram = b
        self.tple = c
        if self.name == 'chicken':
            self.price = b * 10
        else:
            self.price = b * 20

    def eat(self):
        self.gram -= 10

    def sold(self, grams):
        print(f'{grams}만큼 팔림')
        self.gram -= grams

    def __str__(self):
        return f'{self.gram}gram, name: {self.name}, price: {self.price}'

chicken = meat('chicken', 252, 10, 10, 22)
pork = meat('fork', 200)

ori = meat('asdf')

print(chicken.name)
chicken.eat()
chicken.eat()
chicken.sold(32)

print(chicken.gram)
print(chicken.tple)
print(chicken.price)
print(pork.price)
print(chicken)

a = 0
def test():
    print(a)

test()'''

## 2. 문자메시지 서비스를 구축한다, 모델링을 한번 해보자
# sms
# 수신자, 발신자, 내용

class Sms:

    name = 'sms'
    def __init__(self, receiver, sender, content):
        self.receiver = receiver
        self.sender = sender
        self.content = content

    def __str__(self):
        return f' sms 수신자 : {self.receiver}, 발신자 : {self.sender}, 내용 : {self.content}'

    @classmethod
    def send(cls):
        return f'{cls.name} 가 발송되었습니다.'
    
class Lms(Sms): # 자식 클래스

    name = 'lms'
    def __init__(self, receiver, sender, content):
        super().__init__(receiver, sender, content)

    def __str__(self):
        return f' lms 수신자 : {self.receiver}, 발신자 : {self.sender}, 내용 : {self.content}'



s1 = Sms('aiden', 'bpb', 'lasdfl sadlfe rewho')
print(s1)
print(s1.send())
l1 = Lms('g', 're', 'long message')
print(l1)
print(l1.send())

# 부모 : 음료 클래스
# 자식 : 술, 탄산음료, 물


# 이동수단
# 대중교통, 자가용, 몇인승, 용도 등