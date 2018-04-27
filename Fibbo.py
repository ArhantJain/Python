def fibbo(n):
    a=0 #Previous
    b=1 #Present
    c=1
    print(b)
    for i in range(0,n,1):
        c = a+b
        print(c)
        a=b;
        b = c;

num = int(input("Enter the Number"))
fibbo(num)