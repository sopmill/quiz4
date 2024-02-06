class Dog:
    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age

    def title(self):
        return f"{self._name} the {self._breed}"

    def get_age(self):
        return self._age


    def real_age(self):
        return self._age * 7


def main():
    dog1 = Dog("Luna", "Rat Terrier", 11)
    print(dog1.title())
    print(dog1.get_age())

    print(dog1.real_age())


if __name__ == "__main__":
    main()
