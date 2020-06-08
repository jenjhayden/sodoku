class Animal :
    def __init__(dog,n,b,s):
        dog.name=n
        dog.breed=b
        dog.weight=s
        
    def introduce(dog):
        print("Hi I'm ", dog.name, " and I am a ", dog.breed)

    def size(dog):
        if dog.weight<40 :
            print("I am a small dog. I usually weigh under ", dog.weight, " pounds")
        else :
            print("I am not a small dog")

obj1= dog("Fifi","Shih Tzu",56)
obj2= dog("Hawk","Poddle",25)
obj1.introduce()
obj1.size()

obj2.introduce()
obj2.size()