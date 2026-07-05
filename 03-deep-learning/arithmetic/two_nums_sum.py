'''
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target的那两个整数，
并返回它们的数组下标。
'''
import time
#哈希表解法比暴力解法要更高效这个思路很重要
class Solution(object):
    # 哈希表解法
    def twoSum_hashmap(self, nums, target):
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i

    # 暴力解法（双重循环）
    def twoSum_bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 设置数组的规模
n = 1000000  # 生成 100 万个数字
nums = list(range(1, n + 1))  # 生成从 1 到 n 的顺序数组

# 手动设置两个数，使它们的和等于目标值
num1 = 123456  # 可以任意选择一个数
num2 = 1999999 - num1  # 计算使和为 1999999 的另一个数
nums[500000] = num1  # 将 num1 放入数组中
nums[999999] = num2  # 将 num2 放入数组末尾

target = 1999999  # 目标值

solution = Solution()

# 测量哈希表方法的时间
start_time = time.time()
result_hashmap = solution.twoSum_hashmap(nums, target)
end_time = time.time()
print(f"哈希表方法结果: {result_hashmap}, 运行时间: {end_time - start_time:.6f} 秒")

# 测量暴力解法的时间
start_time = time.time()
result_bruteforce = solution.twoSum_bruteforce(nums, target)
end_time = time.time()
print(f"暴力解法结果: {result_bruteforce}, 运行时间: {end_time - start_time:.6f} 秒")
