class Dog:
    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age
    
    @property
    def title(self):
        return f"{self._name} the {self._breed}"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Dog's age must be more than 0")
        self._age = value
    
    @property
    def realAge(self):
        return self._age * 7
    

def main():
    dog1 = Dog("Luna", "Rat Terrier", 11)
    print(dog1.title)
    print(dog1.age)
    print(dog1.realAge)

    
if __name__ == "__main__":
    main()
