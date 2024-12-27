def Hanoi(n , a, b, c):
    if n == 1:
        print("Move disk 1 from rod",a,"To rod",b)
        return
    Hanoi(n-1,a,b,c)
    print("Move disk",n,"from rod",a,"to rod",b)
    Hanoi(n-1,c,b,a)
n = 4
Hanoi(n, 'A', 'C','B')