def product(nums):
    if not nums:
        return 1
    return nums[0] * product(nums[1:])

def squares(nums):
    if not nums:
        return []
    else:
        return [nums[0] ** 2] + squares(nums[1:])

def is_prime(n, i = 2):
    if (n < 2): 
        return False 
    if (n == 2):
        return True
    if (n % i == 0): 
        return False
    if (i * i > n): 
        return True 
  
    return is_prime(n, i + 1) 
