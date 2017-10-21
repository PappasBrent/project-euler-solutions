def f(x):
    ans=1;
    for i in range(1, x):
        ans*=i
    return ans

def sum_of_digits(x):
    ans=0
    for char in str(x):
        ans+=int(char)
    return ans

print(sum_of_digits(f(100)))