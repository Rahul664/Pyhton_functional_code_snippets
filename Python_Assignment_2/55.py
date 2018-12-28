def poundtokg(p):
    try:
        assert (p >= 0), "Negative weight not allowed"
        print("pound is ", p, "converted kg = ", (p * 0.453592))
    except AssertionError as error:
        print(error)

poundtokg(-11)
poundtokg(10)

def pound100kg(p):
  try:
    assert(p>=100), "Weight should be more than or equal to 100"
    print("pound is ", p, "converted kg = ",(p*0.453592))
  except AssertionError as e:
    print(e)

pound100kg(77)
