

def reverseInter(n):
    print n
    if n < 0:
        n=(-1*n)
        return "-"+reverserStr(str(n))
    return reverserStr(str(n))
def reverserStr(str1):
    print str1[1:]
    if len(str1)==1:
        return str1
    else:
        return reverserStr(str1[1:len(str1)])+reverserStr(str1[0])

def reverseNonIter(n):
    m=n
    if n < 0:
        m=n*-1;
        return "-"+reverserNonIterNonNegativee(m)

    return
def reverserNonIterNonNegativee(n):
    k = ''
    while n!=0:
        m=n%10
        n=n/10
        k=k+str(m);
    return k;

# print reverseInter(8123456782)
print reverserNonIterNonNegativee(9)
