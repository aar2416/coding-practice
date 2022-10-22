string = 'abaccaba'
n = len(string)
is_palindrome = True
for i in range(int(n/2)):
    if string[i] != string[n-i-1]:
        is_palindrome = False
        break
if not is_palindrome:
    print("Not a palindrome")
else:
    print("This is palindrome")