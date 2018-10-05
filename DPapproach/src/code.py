def get_the_maxsubarray(l):
    """
    Expired by Kadane's algorithm, uses the dynamic programming technique, the bottom-up approach precisely.
    """

    minimal_sum = 0
    maximal_sum = 0
    current_sum = 0
    size = len(l)

    for i in range(0, size):
        current_sum += l[i]
        minimal_sum = min(minimal_sum, current_sum)
        maximal_sum = max(current_sum - minimal_sum, maximal_sum)

    return maximal_sum
