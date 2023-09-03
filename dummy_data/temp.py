a = 2
b = 5

"""
ans = 81
loop = 27
"""

# resutl = a^b


def cal_pow(num: int, pow: int):
    result = 1
    for x in range(pow):
        result *= num

    return result


def get_sum(array: list, Sum: int) -> list:
    # validations
    result = 0
    pointer = 0

    while pointer < len(array):
        for i in range(len(array)):
            if array[i] == array[pointer]:
                continue
            if array[pointer] + array[i] == Sum:
                result += 1
        pointer += 1

    return result


if __name__ == "__main__":
    # print(f"resutl - {cal_pow(a, b)}")
    print(f"result - {get_sum(array=[-2, -1, 4, 6, 2, 2, 6], Sum=4)}")

    """ input = [-2, -1, 4, 6]
        K = 4
    """
    pass
