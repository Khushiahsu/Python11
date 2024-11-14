#Write a program to print all the prime numbers which come in the range entered by the user?

a = int(input('Enter the lower range number'))
b = int(input('Now enter the upper range number'))

for c in range(a,b+1):
    if c>1:
        for d in range(2,c):
            if(c%d)==0:
                break
        else:
            print(c)
