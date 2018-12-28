#!/bin/python

def file_write_oper():
  #open file in read mode and read all its contents to stdout
  with open("rsh1.txt", "r") as fo:
    print ("reading sample.txt",fo.read() )

  fo.close()
  
  #open file in write mode nad enter 5 new lines to the new file
  with open("rsh1.txt","w") as fin:
    fin.write("Parthiv, Fazal, Mukund to lead in Duleep Trophy \n")
    fin.write("Duleep Trophy 2018 squads announced \n")
    fin.write("three teams picked for Duleep trophy after BCCI had decided to have four\n")
    fin.write("Ambati Rayudu not picked in India A\n")
    fin.write("Duleep Trophy: Selectors avoid gaffe by picking dope-tainted Abhishek Gupta \n")
  fin.close()

  #open the file in append mode and add 5 lines of txt into it
  with open("rsh1.txt","a") as fout:
    fout.write("World's fastest man-made spinning object developed \n")
    fout.write("World's fastest spinning obj could help study quantom mechanics \n")
    fout.write("That is the world's fastest one<F12\n>")
    fout.write("Tiny, floating Dumbbell rotates 60 Billion times in a minute \n")   
    fout.write("This is the fastest rotor humans have ever built and its bendiing our Understandng of physics   \n")

  fout.close()
