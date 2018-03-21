

def fibonacciIter(n):
    if n == 0:
        return -1;
    if n == 1:
        return 1;
    if n==2:
        return 1;
    if n >= 3:
        return fibonacciIter(n-1)+fibonacciIter(n-2);

def fibonacciNonIter(n):
    if n == 0:
        return -1;
    if n == 1:
        return 1;
    if n==2:
        return 1;
    temp1=1;
    temp2=1;
    for index in range(2,n):
        temp=temp1
        temp1=temp2
        temp2=temp+temp1;

    return temp2


print fibonacciNonIter(8)
