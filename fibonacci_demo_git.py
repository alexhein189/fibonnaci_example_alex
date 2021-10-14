#What is Fibbonacci?
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9,...
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34


#Fib(n) = (Fib(n-1) + Fib(n-2))
#Fib(0) =  0
#Fib(1) = 1
# 0 and 1 are our base cases 
#Fib(2) = (Fib(1) + Fib(0)) = 1
#Fib(3) = Fib(2) + Fib(1)
#       = (Fib(1) + Fib(0)) + Fib(1)
#       = (1) + 1 = 2

#Fib(4) = (Fib(3) + Fib(2))
#       = (Fib(2) + Fib(1)) + (Fib(1) + Fib(0))
#       = ((Fib(1) + Fib(0)) + 1) + (1 + 0)
#       = ((1 + 0) + 1) + (1)
#       = (2) + 1 = 3



def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    #main formula of fibonacci sequence
    return fib(n-1) + fib(n-2)


fib_num = int(input("Enter your fib number \n"))
print(fib(fib_num))