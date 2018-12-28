orig_tuple=(10,11,20,40)
lst=[1,2,4]
print("orig_tuple",orig_tuple)
print("lst",lst)
def concat_tuple(a,b):
    b=tuple(b)
    c=a+b
    print("The concatenated tuple",c)
concat_tuple(orig_tuple,lst)
