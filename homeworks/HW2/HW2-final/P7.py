# P7

def positivity(the_function):
    def positivity_inner(*args):
        result = the_function(*args)
        if result <= 0:
            raise Exception
    return positivity_inner


@positivity
def disc(a, b, c):
    disc_result = b**2 - 4*a*c
    print("Trying to compute the discriminant of {0:4.2f}x^2 + {1:4.2f}x + {2:4.2f}:".format(a, b, c))
    print('The result is ', disc_result)
    return disc_result

@positivity
def new_abs(input_value):
    print("Trying to calculate the absolute value of {0:8.6f}:".format(input_value))
    if input_value >= 0:
        result = input_value
    else:
        result = 0 - input_value
    print('The result is ', result)
    return result

@positivity
def difference_with_10(input_value):
    print("Trying to calculate the difference between {0:8.6f} and 10:".format(input_value))
    result = input_value - 10
    print('The result is ', result)
    return result



def test(the_function, the_function_name, *args):
    try:
        the_function(*args)
    except Exception:
        print('The positivity is violated.')


# discriminant: positivity not violated
a = 5; b = 10; c = 2;
test(disc,'calc_disc', a, b, c)
print('')

# discriminant: positivity violated
a = 5; b = 1; c = 2;
test(disc,'calc_disc', a, b, c)
print('')

# absolute: positivity not violated
x = 1;
test(new_abs,'calc_abs', x)
print('')

# absolute: positivity violated
x = 0;
test(new_abs,'calc_abs', x)
print('')

# difference: positivity not violated
input_value = 20;
test(difference_with_10,'calc_diff', input_value)
print('')

# difference: positivity violated
input_value = 5;
test(difference_with_10,'calc_diff', input_value)
print('')
