def five_sort(nums):
  count = 0
  for i in (range(len(nums) - 1, -1, -1)):
    if nums[i] == 5:
      count += 1
      nums.remove(nums[i])
  for i in range(count):
    nums.append(5)
  return nums
  