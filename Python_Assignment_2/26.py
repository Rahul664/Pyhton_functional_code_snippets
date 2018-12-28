import base64
print("Enter the encoding to be used")
print("1 for base64")
print("2 for utf-16")
print("3 for utf-32")
en=int(input())
str_input=input("Enter the string to encode")

if en==1:
    str_base64_en = base64.b64encode(str_input.encode())
    print("Encoded string",str_base64_en)
elif en==2:
    str_utf_8=str_input.encode('utf-16','strict')
    print("Encoded string",str_utf_8)

elif en==3:
    str_utf_32=str_input.encode('utf-32','strict')
    print("Encoded string",str_utf_32)

if en==1:
    str_base64_de=base64.b64decode(str_base64_en)
    print("Decoded string",str_base64_de)
elif en==2:
    str_utf_8_de=str_utf_8.decode('utf-16','strict')
    print("Decode string",str_utf_8_de)
elif en==3:
    str_utf_32_de=str_utf_32.decode('utf-32','strict')
    print("Decode string",str_utf_32_de)
