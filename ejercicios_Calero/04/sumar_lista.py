def sumar(nums):
    if not isinstance(nums, list):
        raise TypeError("Debe ser una lista")
    return sum(nums)

print(sumar([1, 2, 3]))