a='teeshaTTT'
t=a.swapcase()
print(t)
def split_and_join(line):
    # write your code here
    a=line.split()
    b='-'.join(a)
    return b
def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')
def mutate_string(string, position, character):
    new_string=string[:position]+character+string[position+1:]
    return new_string
#to count the occurence of the given substring in the string
def Count(string1,substring):
    count=0
    if len(substring)>len(string1):
        return count
    else:
        for i in  range(0,len(string1)):
            if string1[i:].startswith(substring):
                count+=1
        print(count)



Count('abcdcdc','cdc')
# s = input()
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isupper())
# print(s.islower())
#abbc: ac
def duplicates(string):
    a=[]
    for i in range(len(string)):
        if len(a)!=0 and a[-1]==string[i]:
            a.pop()
        else:
            a.append(string[i])

    print( ' '.join(a))
duplicates('abbc')
#program for the palindrome string
def sentence_palindrome(string1):
    a=string1.strip()
    b=a.casefold()
    c=b.replace(' ','')
    d=c[::-1]
    if d==c:
        print('palindrome sentence')
    else:
        print('not so')
    print(c)

sentence_palindrome('   VanShika saxena')
sentence_palindrome('abc  cba')
#function for getting permutation
from itertools import permutations
def perm(word):
    words=[''.join(p) for p in permutations(word)]
    print(words)
perm('abc')
perm('ht')


def lengthOfLongestSubstring(str):
    n = len(str)
    res = 0
    for i in range(n):
        visited = [0] * 256
        for j in range(i, n):
            if (visited[ord(str[j])] == True):
                break

            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True

        visited[ord(str[i])] = False

    return res



    s = "Hello"
    print(lengthOfLongestSubstring(s))
