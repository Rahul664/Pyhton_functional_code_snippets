f=open("rsh.txt", "r")
print(f.read())
f.close()

f=open("rsh2.txt","w")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry\n "
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n")
f.close()

f=open("rsh2.txt","a")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry\n "
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n"
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry\n")
f.close()
