# Naf (Nafiyu Murtaza), Alex (Sasha Murokh), Jonathan (Jonathan Metzler)
# No Z's In Our Name
# SoftDev
# K04 -- Python Lists
# 2024-09-17
# Time: N/A

# READ: The function names indicate the problem in Codingbat.

def first_last6(nums):
  return nums[0]==6 or nums[len(nums)-1]==6

def same_first_last(nums):
  if len(nums)>0:
    return nums[0]==nums[len(nums)-1]
  return False

def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0]==b[0] or a[len(a)-1]==b[len(b)-1]

def sum3(nums):
  return nums[0]+nums[1]+nums[2]

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  m = max(nums[0], nums[2])
  return [m, m, m]

def sum2(nums):
  if len(nums)>1:
    return nums[0]+nums[1]
  elif len(nums)==1:
    return nums[0]
  else:
    return 0

def middle_way(a, b):
  return [a[1],b[1]]

def make_ends(nums):
  return [nums[0], nums[len(nums)-1]]

def has23(nums):
  return (2 in nums) or (3 in nums)