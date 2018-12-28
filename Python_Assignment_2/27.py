check=input("Enter the string to check if its pallindrome")
rev="".join(reversed(check))
if check==rev:
    print("The sting is pallindrome")
else:
    print("The sting is not a pallindrome")
