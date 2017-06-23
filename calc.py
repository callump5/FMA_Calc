choice = raw_input("Enter calculation you want to use ")

# Force =  Mass * Acceleration
def force():
    mass = float(raw_input("Enter mass of object in kg: "))
    acc = float(raw_input("Enter acceleration of object in m/s^2: "))

    def do_calc(mass, acc):
        force = mass * acc
        print str(force) + "N"

    do_calc(mass, acc)

#  Mass = Force / Acceleration
def mass():
    force = float(raw_input("Enter force of object in N: "))
    acc = float(raw_input("Enter acceleration of object in m/s^2: "))

    def do_calc(force, acc):
        mass = force / acc
        print str(mass) + "Kg"

    do_calc(force, acc)

# Mass = Force / Acceleration
def acc():
    force = float(raw_input("Enter force of object in N: "))
    mass = float(raw_input("Enter mass of object in kg: "))

    def do_calc(force, mass):
        acc = force / mass
        print str(acc) + "M/s^2"

    do_calc(mass, force)



if choice == str('force'):
    force()
elif choice == str("mass"):
    mass()
elif choice == str("acceleration"):
    acc()