def add( firstName: str, lastName: str ):
    firstName.capitalize()
    return firstName + " " + lastName

fname = "Bill"
lname = "Gates"

name = add(fname.capitalize(),lname) #capitalize the firstname
print(name)