# Naf (Nafiyu Murtaza), Alex (Sasha Murokh), Jonathan (Jonathan Metzler)
# No Z's In Our Name
# SoftDev
# K04 -- Python Lists
# 2024-09-17
# Time: N/A

# READ: The function names indicate the problem in Codingbat.

def count_evens(nums):
  counter =0
  for item in nums:
    if item%2==0:
      counter+=1
  return counter

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  return (sum(nums)-max(nums)-min(nums))/(len(nums)-2)

def sum13(nums):
  sum =0
  index1 =0
  while index1<len(nums):
    if nums[index1]==13:
      index1+=2
    else:
      sum+=nums[index1]
      index1+=1
  return sum

def sum67(nums):
  sum =0
  six = False
  for item in nums:
    if (item==6):
      six = True
    elif (item==7):
      if (six==True):
        six = False
      else:
        sum+=7
    else:
      if (six==False):
        sum+=item
  return sum

def has22(nums):
  i =0
  while i<(len(nums)-1):
    if nums[i]==2 and nums[i+1]==2:
      return True
    i+=1
  return False