i=1
while i<=5:
    s=1
    while s<=10:
        print(s)
        s=s+1
    i=i+1
print(i)

for q in range(15,20):
    for a in range(8,15):
        print(a)

    print(q)

#Write a program to check how many times a character is repeated in a word?


a = input('Enter a word')
b = input('Please enter your own character')

c = 0
d = 0
while (c<len(a)):
    if(a[c]==b):
        d=d+1
    c=c+1
print('The total number of times', b,'has occured',d)
