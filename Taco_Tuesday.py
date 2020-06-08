class Animal :
    def __init__(self,n,b,s):
        self.name=n
        self.breed=b
        self.weight=s
        
    def introduce(self):
        print("Hi, my name is ", self.name," and I am a", self.breed)

    def size(self):
        if self.weight<40 :
            print("I am a small dog. I can fit in there.")
        else :
            print("Yeah.... you're going to need a bigger bag...")

dog1= Animal("Fifi","Brussells Grifton",12)
dog2= Animal("Hawk","Siberian Husky",50)

dog1.introduce()
dog1.size()

dog2.introduce()
dog2.size()
