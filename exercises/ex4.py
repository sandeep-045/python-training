cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # result after the subtraction of cars variable and drivers is assigned to  cars_not_driven.
cars_driven = drivers #value of drivers variable is assigned to cras_driven. 
carpool_capacity = cars_driven * space_in_a_car 
average_passengers_per_car = passengers / cars_driven # A float value is assigned to average_passengers_per_car.
print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
