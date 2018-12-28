from stringpackage import bubblesort
from stringpackage import palindrome
from stringpackage import vowel

#bubblesort module
bsort_elem = int(input("enter the no of elements"))
bsort_l1=[]
for i in range(bsort_elem):
  ob=int(input("enter the elements"))
  bsort_l1.append(ob)

print("the list before sorting:", bsort_l1)
bubblesort.bubblesort(bsort_l1)

#vowel:
print( "Printing the number of vowels in a string/line:")
v_name=input("enter a string :")

vowel.vowel(v_name)


#palindromemodule
p_str1=input("enter a string to be checked for palindrome:")
print(p_str1)

palindrome.palindrome(p_str1)

