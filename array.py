# def twoSum(nums,target):
#     for i in range (0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 print( i,j)
#
#
# twoSum(nums=[3,2,4],target=6)
# twoSum(nums = [3,3], target = 6)
# twoSum(nums = [2,7,11,15], target = 9)
# twoSum(nums=[2,1,3],target=5)
#
#
# def lengthOfLongestSubstring( s: str) -> int:
#     charset = set()
#     result = 0
#     l = 0
#     for r in range(len(s)):
#         while s[r] in charset:
#             charset.remove(s[l])
#             l += 1
#         charset.add(s[r])
#         result = max(result, r - l + 1)
#     print(result)
# lengthOfLongestSubstring('abcabcbb')
#
# def plusMinus(arr):
#     # Write your code here
#     count_positive=0
#     count_negative=0
#     count_zero=0
#     for i in arr:
#         if i>0:
#             count_positive+=1
#         elif i<0:
#             count_negative+=1
#         else:
#             count_zero+=1
#     total_count=len(arr)
#     a=count_positive/total_count
#     b=count_negative/total_count
#     c=count_zero/total_count
#     print(("%.6f")%a)
#     print(("%.6f")%b)
#     print(("%.6f")%c)
#
#
# def miniMaxSum(arr):
#     # Write your code here
#     a = sorted(arr)
#     min_sum = sum(a[:4])
#     max_sum = sum(a[1:])
#     print(min_sum, max_sum)
#
#
# def timeConversion(s):
#     h = int(s[0:2])
#
#     if s[-2] == 'P' or s[-2] == 'p':
#         if h != 12:
#             h = 12 + h
#         else:
#             h = h
#         return (str(h) + s[2:8])
#     else:
#         if h == 12:
#             return ("00" + s[2:8])
#         else:
#             return (s[:8])
#
#
# s = input()
# result = timeConversion(s)
# print(result)
#
# def lonelyfunction(a):
#     for i in a :
#         b=a.count(i)
#         if b==1:
#             return i
#
# def diagnoldifference(arr):
#     sum1=0
#     sum2=0
#     for i in range(len(arr)):
#         sum1+=arr[i][i]
#     for i in range(len(arr)):
#         sum2+=arr[i][len(arr)-i-1]
#     a=abs(sum1-sum2)
#     return a
#
#
# def countingSort(arr):
#     # Write your code here
#     b = [0] * 100
#     for i in arr:
#         b[i] += 1
#     return b
#
# def gridchallenge(grid):
#     n=len(grid)
#     m=len(grid[0])
#     grid[0]=sorted(grid[0])
#     for i in range(n):
#         grid[i]=sorted(grid[i])
#         for j in range(m):
#             if grid[i-1][j]>grid[i][j]:
#                 return('No')
#     return('yES')
# a=gridchallenge(['mpxz','abcd' ,'wlmf'])
# print(a)
def superDigit(n, k):
    res=0
    temp=n
    while temp>9:
        for i in range(k):
            a=temp%10
            res+=a
            temp=res
    return(res)
a=superDigit(9875,4)
print(a)