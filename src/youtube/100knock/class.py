#class
class Person:
    nationality = 'Japan'
    
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')

person = Person()
person.nationality
person.say_hello()

#コンストラクタ
class Person:
    nationality = 'Japan'

    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')

    def say_myname(self):
        print(f'私の名前は{self.name}です')

mei = Person('mei')
mei.nationality
mei.name
mei.say_myname()

#クラスの継承
class Kid(Person):
    def say_hello(self, age):
        print(f'私の名前は{self.name}です。年齢は{age}です')

kid = Kid('natsu')
kid.name
kid.nationality
kid.say_hello(12)

#private, public
class Person:
    __nationality = 'Japan'

    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.__nationality}です')

    def __say_myname(self):
        print(f'私の名前は{self.name}です')

mei = Person('mei')

mei.__nationality   #privateになっているためこれはエラーになる
mei.__say_myname()  #これもエラー
mei.say_hello()  #これは呼び出せる、内部で__nationalityが使われてるのは大丈夫