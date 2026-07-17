num= input("Enter a value:")
if num == num[::-1]:
    print("Palindrome",num)
else:
    print("Not palindrome",num)