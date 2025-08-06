num=int(input("Enter a number"))
bin=''

if num==0:
    bin='0'
while num>0:
    bin = str(num%2)+bin
    num = num//2

print(bin)