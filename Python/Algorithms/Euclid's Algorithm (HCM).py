#Euclid's Algorithm
#Abhinandan Raj

    #Algorithm accepts first number "m"
    #Algotithm accepts second number "n"
    #Algorithm returns highest common factor


def algorithmE(m,n):
    r=m%n
    if r==0:
        return n
    else:
        m=n
        n=r
        return algorithmE(m,n)

#Example usage
print(algorithmE(544,119))