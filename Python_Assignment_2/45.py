ip=input("Enter the string to check for pallindorme")
def palindrome(ip):
  len1= len(ip)
  if ip == ip[::-1]:
    print("The string  is palindrome" )
  else:
    print("The string  is not palindrome")

palindrome(ip)
