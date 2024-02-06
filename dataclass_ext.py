from dataclasses import dataclass

@dataclass
class SummerJobs:
    place: str
    job: str
    numMonths: int

    def __out__(self) ->str:
        return f"{self.place}, {self.job}, {self.numMonths}"


    def __bestJob__(self) ->str:
        answer = input("Do you perfer the beach or the mountains? ")
        if (answer.lower() == "beach"):
            return("You would enjoy working at CLimbWorks in TN!")
        elif (answer.lower() == "mountains"):
            return("You would enjoy working at Camp Miniwanca in MI!")
        else:
            return("Invalid input.")


def main ():
    summer22 = SummerJobs(place="Michigan", job="Camp Counsler", numMonths=2)
    print (summer22.__out__())

    summer23 = SummerJobs(place="Tennessee", job="Zipline Tour Guide", numMonths=3)
    print (summer23.__out__())

    print (summer23.__bestJob__())

    
if __name__ == "__main__":
    main()