def SumE(iNo):
    print(iNo)
    iSum=0
    iDigit=0
    while int(iNo)>0:
        iDigit=int(iNo)%10
        if iDigit%2==0:
            iSum=iSum+iDigit;
        iNo=int(iNo)/10
        
    return iSum
    


def main():
    try:
        no=int(input("enter the number"))
        validNum=isinstance(no,int);
        
        if(no<0):
            print("negative numbers not allowed")
        else:
            iRet=SumE(no)
            print("count of digit is: ",iRet)
    except:
        print("invalid number")

    

if __name__=="__main__":
    main()