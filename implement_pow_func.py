a= int(input("Enter A: "))
b = int(input("Enter B: "))
c =int(input("Enter C: "))
def pow(a,b,c):
    if b==0:return 1
    if b==1: return a

    if b%2==0:
        p = pow(a, b / 2, c)
        return (p*p)%c
    else:
        p = pow(a, b / 2, c)
        return (p*p*a)%c
print(pow(a,b,c))