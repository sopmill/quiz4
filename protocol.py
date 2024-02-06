from typing import Protocol
import os

class RockClimbing(Protocol):
    def routeSetting(self, name:str, grade:str)->None:
        ...
    def load(self, grade:int, skill:int)->None:
        ...

class TopeRoping:
    def __init__(self,name:str) -> None:
        self.name = name

    def routeSetting(self,name:str, grade:str) -> str:
        print(name + grade)

    def betaLoading(self, grade:str, skill:str)->None:
        self.send = skill > grade
        
class Bouldering:
    def __init__(self, name:str, grade:str):
        self.name=name
        self.grade=grade

    def routeSetting(self, name:str, grade:str):
        print(name + " " + grade)

    def betaLoading(self, grade:str, skill:str):
        self.send = skill > grade

def main():
    name = "Slippery Slopes"
    grade = "11a"    

    bouldering : RockClimbing = Bouldering(name, grade) #<-- Magic
    boulderingName= Bouldering(name, grade)
    boulderingName.routeSetting(name, grade)


if __name__=="__main__":
    main()