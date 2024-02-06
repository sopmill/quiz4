from dataclasses import dataclass

@dataclass
class SummerJobs:
    place: str
    job: str
    numMonths: int

    def __out__(self) ->str:
        return f"{self.place}, {self.job}, {self.numMonths}"



def main ():
    summer22 = SummerJobs(place="Michigan", job="Camp Counsler", numMonths=2)
    print (summer22.__out__())

    summer23 = SummerJobs(place="Tennessee", job="Zipline Tour Guide", numMonths=3)
    print (summer23.__out__())


if __name__ == "__main__":
    main()