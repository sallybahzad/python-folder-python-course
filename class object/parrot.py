#create class
class parrot:
    #class attribute
    species="bird"
    #instance attribute
    def __init__(self,name,age):
     self.name=name
     self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

