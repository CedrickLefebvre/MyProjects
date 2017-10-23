def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2
    if even_odd == True:
        print("VRAI")
    else :
        print('FAUX')

even_odd(4)
even_odd(3)
even_odd(100)
even_odd(1)
