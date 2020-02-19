import random as Randy  #Hi Randy

def gen_random(digits=6, d_range=6, n=1):
    """This will generate n random numbers of length digits, with the
    difference between each digit being less than or equal to d_range"""

    numbers_list = []

    for c in range(n):
        number = ""
        digit_list=[]
        digit_list.append(Randy.randint(0,9))
        #Put an initial value into the list

        a = 0
        while a < digits-1:
            #x = Randy.randint(0,9)
            #if abs(digit_list[-1]-x) <= d_range:
            #    digit_list.append(x)
            #    a = a + 1
            m,n = 0,9
            #x = [Randy.randint(m,n) for a in range(digits-1)]
            if digit_list[-1] - d_range > 0:
                m = digit_list[-1] - d_range
            if digit_list[-1] + d_range < 9:
                n = digit_list[-1] + d_range
            x = Randy.randint(m,n)
            digit_list.append(x)
            a = a + 1

        b = 0
        while b < len(digit_list):
            digit_list[b]=str(digit_list[b])
            b = b + 1
        number = number.join(digit_list)

        #if len(number) != digits:
        #    print(f"Number {number} failed length test.")
        #numbers_list.append(int(number))
        #The string to int conversion removes leading zeros.
        numbers_list.append(number)

    print(numbers_list)

#gen_random(6,6,20)
