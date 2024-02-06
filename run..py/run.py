from travelIceland.iceland import icelandFunction
from travelGreece.greece import greeceFunction
from travelThailand.thailand import thailandFunction

def main():
    ice = icelandFunction()
    gre = greeceFunction()
    tha = thailandFunction()

    print(f"Top three choices are {ice} {gre} {tha}")

if __name__ == "__main__":
    main()
