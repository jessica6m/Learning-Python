"""
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
"""
print "The Calculator is starting up"
option = raw_input("Enter C for Circle or T for Triangle: ")
if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print "Area: %f" % area
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area: %f" % area
else:
  print "Error! Invalid shape."
  
print "Exiting..."