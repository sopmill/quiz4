import argparse

def q1() -> None: 	
    parser=argparse.ArgumentParser() 	
    parser.add_argument(help='Enter a string: ',dest='string',type=str)         	
    parser.add_argument(help='Enter an int: ',dest='number',type=int) 
    parser.add_argument(help='Enter a float: ',dest='float',type=float)         	
  
	
    args = parser.parse_args()  	

    words=args.string 	
    numbers=args.number  	
    decimals=args.float

    print("String is: ", words) 	
    print("Number is: ", numbers)
    print("Float is: ", decimals)

if __name__=='__main__': 	
    q1()
