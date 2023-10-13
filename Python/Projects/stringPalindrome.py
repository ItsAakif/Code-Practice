// Python Code for checking is String Palindrome or not

def isPalindrome(S):
  j = -1
  n = len(S)//2
  
  for i in range(n):
      if S[i] != S[j]:
          return 0
      j -= 1
  return 1

string = input()
check = isPalindrome(string)

if check:
  print('Given string is palindrome')
else:
  print('Given string is not palindrome')
