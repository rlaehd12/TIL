class meat:
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

test()