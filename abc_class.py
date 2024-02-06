from abc import ABC , abstractmethod
import os

class RockClimbing(ABC):

    @abstractmethod
    def routeSetting(self, name, grade):
        pass

    @abstractmethod
    def betaLoading(self, grade, skill):
        pass

class TopRoping(RockClimbing):
    def __init__(self,name):
        self.name = name

    def routeSetting(self, name, grade):
        print(name + grade)

    def betaLoading(self, grade, skill):
        self.send = skill > grade
        

class Bouldering(RockClimbing):
    def __init__(self, name, grade):
        self.name=name
        self.grade=grade

    def routeSetting(self, name, grade):
        print(name + " " + grade)

    def betaLoading(self, grade, skill):
        self.send = skill > grade


def  main():
    name = "Slippery Slopes"
    grade = "11a"

    boulderingName= Bouldering(name, grade)
    boulderingName.routeSetting(name, grade)

if __name__=="__main__":
    main()