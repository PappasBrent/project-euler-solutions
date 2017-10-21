# def f(x):
#     if x in [1,2]:
#         return 1
#     else:
#         return f(x-1) + f(x-2)

# i=1

# while int(f(i) / 10) < 10*2:
#     i+=1

# print(i)




def f(x):

    # f(x - 1)
    fxm2 = 1
    # f(x - 2)
    fxm1 = 1

    # Starts at two since the first two values of f(x)
    # are already known
    for i in range(2,x):
        # f(x) = f(x - 1) + f(x - 2)
        fx = fxm2+fxm1

        # The value that was f(x - 1) is now f(x - 2)
        fxm2 = fxm1
        # The value that was f(x) is now f(x - 1)
        fxm1 = fx
        

    return (fx)

i=3

while len(str(f(i)))<1000:
    i+=1

print(i)