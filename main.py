
def find_factors(num):
    '''
    Find all factors of a positive integer
    :param num: positive integer
    :return: list of all factors
    '''

    if isinstance(num, int) == False and num <= 0:
        return None
    else:
        result = [num]
        for i in range(1, int(num/2) + 1):
            if num % i == 0:
                result.append(i)
        result.sort()
        return result

print(find_factors(56564))
