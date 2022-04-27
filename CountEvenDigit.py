def CountE(iNo):
    print(iNo)
    iCnt=0
    iDigit=0
    while int(iNo)>0:
        iDigit=int(iNo)%10
        if iDigit%2==0:
            iCnt=iCnt+1;
        iNo=int(iNo)/10
        
    return iCnt
    


def main():
    try:
        no=int(input("enter the number"))
        validNum=isinstance(no,int);
        
        if(no<0):
            print("negative numbers not allowed")
        else:
            iRet=CountE(no)
            print("count of digit is: ",iRet)
    except:
        print("invalid number")

    

if __name__=="__main__":
    main()