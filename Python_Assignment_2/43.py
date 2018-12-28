def search(*a):
    list1 = [1 ,2 ,3 ,34 ,45 ,56 ,67 ,768 ,788 ,76 ,75]
    for arg in a:
        for i in list1:
            if arg == i:
                print("Element %f found in the list" % arg)
                break
        else:
            print("Element %f is not found in the list" % arg)

search(890)
search(1 ,2)
search(-23)
search(00)
search(3.233)
search(2 ,3 ,7777)
