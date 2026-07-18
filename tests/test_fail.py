from project.animals import Cat

cat = Cat(name="Garfield",city="Davis",age=1978)

def test_Cat_info():
    assert (cat.display_info()!="")
    assert (cat.display_info()=="Garfield Davis 1978")

def test_Cat_name():
    assert (cat.get_name()=="Cat's name is Garfield")
    # assert (cat.get_name()=="Cat's name is not John") # Uncomment to see what happens if test fails.