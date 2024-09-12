import math

def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    ### YOUR CODE HERE ###

    pi_approximation = 0

    a_n = 1
    b_n = 1 / math.sqrt(2)
    p_n = 1
    t_n = 1 / 4
    upper_bound = 10

    pi_approximation = ((a_n + b_n) ** 2) / (4 * t_n) #inital calculation of pi
    actual_error = abs(pi_approximation - math.pi) #determines the error in the initial calculation

    while target_error < actual_error: #when the actual error is greater than the target error the program will increase its upper bound until the approximation is closer
        upper_bound += 1
        for x in range(1, upper_bound):
            a = (a_n + b_n) / 2
            b = math.sqrt(a_n * b_n)
            p = 2 * p_n
            t = t_n - p_n * (a - a_n) ** 2

            a_n = a
            b_n = b
            p_n = p
            t_n = t
        pi_approximation = ((a_n + b_n) ** 2) / (4 * t_n)
        actual_error = abs(pi_approximation - math.pi)

    return pi_approximation

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
