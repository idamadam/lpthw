# Add 100 cars to system
cars = 100
# Define car capacity
space_in_a_car = 4.0
# Add 30 Drivers
drivers = 30
# Add 90 passengers
passengers = 90
# Calculate cars not driven by removing cars with drivers
cars_not_driven = cars - drivers
# Equate cars driven to number of drivers available
cars_driven = drivers
# Find available carpool space by multiplying cars driven by car capacity
carpool_capacity = cars_driven * space_in_a_car
# Find average passngers required by dividing passengers over cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."
