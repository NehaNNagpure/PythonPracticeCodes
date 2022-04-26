def DisplayFactors(iNo):
    print(iNo)
    for i in range(1,iNo+1):
        if(iNo%i==0):
            print(i)
            
def main():

    try:
        no=int(input("enter the number"))
        validNum=isinstance(no,int);
        if(no<0):
            print("negative numbers not allowed")
        else:
            DisplayFactors(no)
    except:
        print("invalid number")
if __name__=="__main__":
    main()