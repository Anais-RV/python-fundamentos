def promedio(nums: list[float]) -> float:
    if not isinstance(nums, list):
        raise TypeError("nums debe ser una lista")
    if len(nums) == 0:
        raise ValueError("La lista no puede estar vacía")
    return sum(nums) / len(nums)

print(promedio([5, 6, 8, 9]))
print(promedio([9]))
print(promedio([]))