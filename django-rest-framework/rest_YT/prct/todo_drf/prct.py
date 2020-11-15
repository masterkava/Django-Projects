# prime no
def func(n):
    for i in range(2, n):
        if n%i==0:
            print(n, "is Not Prime")
            break
    else:
        print(n, "is Prime Number")

# func(13)
# func(9)
# func(917463527957462547473)
