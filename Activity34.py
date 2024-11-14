#Write a program to calculate the product of the middle digits of a number?
a = int(input('Enter the number:'))
t = a
numlen = 0

while t>0:
    numlen = numlen+1
    t=int(t/10)
if numlen>=4:
    numlen=int(numlen/2)
    b = 0
    while a>0:
        rem = a%10
        if b==numlen:
            mid = rem
        elif b==(numlen-1):
            mid2=rem
        a = int(a/10)
        b = b+1
    prod=mid*mid2
    print(prod)
else:
    print('It is not a 4 or more digit number')