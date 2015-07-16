# There are 100 cars
cars = 100
# Each car has 4 spaces
space_in_a_car = 4.0
# There are 30 drivers
drivers = 30
# Thre are 90 passengers
passengers = 90
# The number of cars not driven is the total number of cars minus the number of drivers
cars_not_driven = cars - drivers
# Each drive will drive a car
cars_driven = drivers
# The total car pool capacity is the number of driven cars multiplied by the spaces in the car
carpool_capacity = cars_driven * space_in_a_car
# The average passengers per car is number of passengers divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."