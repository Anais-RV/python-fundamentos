def sumar(nums):
    if not isinstance(nums, list):
        raise TypeError("nums debe ser lista")
    total = 0
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    print(sumar([1, 2, 3, 4]))
