#a short menu based programme to understand logical operats,conditions and loops.
#python does not have switch case,so  MENU CAN BE FORMED using infinite loop
while True:
    print('''                --Menu--
    1)1 for Prime number check
    2)2 for Palindrome check
    3)any key to quit
    ''')
    choice=input("Enter your choice")
    if(choice=='1'):
        print("----Prime num check-----")
        n=int(input())
        c=0
        for i in range (1,n+1):
            if n % i==0:
                c+=1

        if c!=2:
            print("Not a prime num")
            #print(c)
        else:
            print("Prime num")
            #print(c)

    elif choice=='2':
        print("----Palindrome check-----")
        n=int(input())
        temp=n
        rev=0
        while temp!=0:
            lastdig=temp%10
            rev=(rev*10)+lastdig
            temp=temp//10
        print (temp)
        if(rev==n):
            print('Palindrome yes')
        else:
            print("Palindrome no")
    else:
    
            print('Thank you')
            break            


        #print (type(range))        