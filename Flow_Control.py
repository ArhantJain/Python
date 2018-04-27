# Flow Control

# if else

marks = 75
if( marks > 80):
    print("Grade A")

elif ( marks > 60 and marks < 80):
    print("Grade B")

elif( marks > 40 and marks < 60):
    print( " Grade C")

else:
    print("Grade D")

# While

num = int(input('Enter the value of n='))
if ( num <= 0):
    print("Invalid Number")
else:
    sum=0
    while(num>0):
        sum += num
        num = num -1

print(sum)


# For Loop

# for quant in range  (0,n,1):

#    Break

count = 0
while True:
    count = count + 1
    print(count)
    if( count == 10):
        break;
# Continue